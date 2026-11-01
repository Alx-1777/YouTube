import sys, json, os, subprocess
from PIL import Image, ImageDraw, ImageFont
S, src, a, b, name, t1, t2 = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7]
cues = json.load(open(f"{S}/final.json"))
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
W, H = 1080, 1920
d = f"{S}/{name}"; os.makedirs(d, exist_ok=True)
def F(sz, i=1): return ImageFont.truetype(FONT, sz, index=i)
def wrap(dr, text, font, maxw):
    lines, cur = [], ""
    tokens = text.split(" ") if text.isascii() else list(text)
    sep = " " if text.isascii() else ""
    for tk in tokens:
        t = (cur + sep + tk) if cur else tk
        if dr.textlength(t, font=font) > maxw and cur: lines.append(cur); cur = tk
        else: cur = t
    return lines + [cur]
def card(en=None, zh=None):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((60, 110, W-60, 370), 28, fill=(0, 0, 0, 150))
    y = 135
    for ln in wrap(dr, t1, F(64), 900):
        dr.text((W/2, y), ln, font=F(64), fill="white", anchor="ma"); y += 78
    for ln in wrap(dr, t2, F(52), 900):
        dr.text((W/2, y), ln, font=F(52), fill=(255, 214, 10), anchor="ma"); y += 64
    dr.text((W/2, 1800), "Full video on my channel · 完整版在主页", font=F(36, 0), fill=(255,255,255,220), anchor="ma", stroke_width=3, stroke_fill="black")
    if en:
        y = 1430
        for ln in wrap(dr, en, F(58), 960):
            dr.text((W/2, y), ln, font=F(58), fill="white", anchor="ma", stroke_width=5, stroke_fill="black"); y += 70
        for ln in wrap(dr, zh, F(54), 960):
            dr.text((W/2, y+8), ln, font=F(54), fill=(255, 214, 10), anchor="ma", stroke_width=5, stroke_fill="black"); y += 66
    return im
seq, t, k = [], 0.0, 0
dur = b - a
blank = f"{d}/blank.png"; card().save(blank)
for c in cues:
    s, e = max(c[0]-a, 0), min(c[1]-a, dur)
    if e <= 0 or s >= dur: continue
    if s > t: seq.append((blank, s-t))
    p = f"{d}/c{k}.png"; card(c[2], c[3]).save(p); k += 1
    seq.append((p, e-max(s,t))); t = e
if t < dur: seq.append((blank, dur-t))
with open(f"{d}/list.txt", "w") as f:
    for p, du in seq: f.write(f"file '{p}'\nduration {du:.3f}\n")
    f.write(f"file '{seq[-1][0]}'\n")
cw, ch = 984, 1750
vf = f"[0:v]crop={cw}:{ch}:{(3840-cw)//2}:0,scale={W}:{H},setsar=1[v];[1:v]format=rgba[s];[v][s]overlay=0:0:format=auto,format=yuv420p"
subprocess.run(["ffmpeg","-v","error","-y","-ss",str(a),"-t",str(dur),"-i",src,"-f","concat","-safe","0","-i",f"{d}/list.txt",
  "-filter_complex",vf,"-r","30","-c:v","libx264","-preset","medium","-crf","20","-c:a","aac","-b:a","160k","-shortest",
  os.path.expanduser(f"~/Desktop/{name}.mp4")], check=True)
print("done", name, round(dur,1))
