import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
S=sys.argv[1]; out=sys.argv[2]
K=2; W,H=1280*K,720*K
HN='/System/Library/Fonts/HelveticaNeue.ttc'
bg=Image.new('RGB',(W,H),(10,11,16))
# subtle radial glow behind GPU
glow=Image.new('L',(W,H),0); gd=ImageDraw.Draw(glow)
gd.ellipse((-200*K,330*K,820*K,900*K),fill=120); glow=glow.filter(ImageFilter.GaussianBlur(120*K))
bg.paste(Image.new('RGB',(W,H),(40,90,255)),(0,0),glow)
# face: right side
f=Image.open(f'{S}/face.png').convert('RGB')  # 3840x2160
fx,fy,fw=1330,230,1240; fh=int(fw*720/600)
face=f.crop((fx,fy,fx+fw,fy+fh)).resize((600*K,720*K),Image.LANCZOS)
face=ImageEnhance.Brightness(face).enhance(0.92); face=ImageEnhance.Contrast(face).enhance(1.12); face=ImageEnhance.Color(face).enhance(1.05)
m=Image.new('L',face.size,255); md=ImageDraw.Draw(m)
for x in range(200*K): md.line((x,0,x,face.size[1]),fill=int(255*(x/(200*K))**1.4))
bg.paste(face,(W-600*K,0),m)
d=ImageDraw.Draw(bg)
# GPU card
def rr(b,r,**k): d.rounded_rectangle([v*K for v in b],r*K,**k)
gx,gy,gw,gh=70,430,560,210
rr((gx+10,gy+gh-4,gx+gw-40,gy+gh+22),6,fill=(150,155,165))   # PCIe edge / bracket strip
for i in range(14): rr((gx+40+i*30,gy+gh+2,gx+58+i*30,gy+gh+20),2,fill=(212,175,55))
rr((gx,gy,gx+gw,gy+gh),22,fill=(32,34,40),outline=(90,95,105),width=3*K)
rr((gx+gw-10,gy-20,gx+gw+14,gy+gh+30),6,fill=(170,175,185))  # bracket
for i in range(3):
    cx=gx+100+i*180; cy=gy+gh/2; R=82
    d.ellipse([(cx-R)*K,(cy-R)*K,(cx+R)*K,(cy+R)*K],fill=(18,19,23),outline=(70,74,84),width=3*K)
    for b in range(9):
        a=b*2*math.pi/9
        pts=[]
        for t in range(12):
            rr_=18+t*5.5; aa=a+t*0.06
            pts.append(((cx+rr_*math.cos(aa))*K,(cy+rr_*math.sin(aa))*K))
        d.line(pts,fill=(95,100,112),width=9*K)
    d.ellipse([(cx-18)*K,(cy-18)*K,(cx+18)*K,(cy+18)*K],fill=(50,53,60))
rr((gx+20,gy+10,gx+gw-30,gy+16),3,fill=(40,120,255))  # accent strip
# text
F1=ImageFont.truetype(HN,140*K,index=9)
d.text((64*K,40*K),'WHY AI',font=F1,fill='white')
d.text((64*K,180*K),'NEEDS THIS',font=F1,fill=(255,214,10))
# arrow from text down to GPU
def arrow(p0,p1,c,w):
    d.line([p0[0]*K,p0[1]*K,p1[0]*K,p1[1]*K],fill=c,width=w*K)
    ang=math.atan2(p1[1]-p0[1],p1[0]-p0[0]); L=44
    pts=[(p1[0]+12*math.cos(ang),p1[1]+12*math.sin(ang)),
         (p1[0]-L*math.cos(ang-0.5),p1[1]-L*math.sin(ang-0.5)),
         (p1[0]-L*math.cos(ang+0.5),p1[1]-L*math.sin(ang+0.5))]
    d.polygon([(x*K,y*K) for x,y in pts],fill=c)
arrow((705,362),(600,428),(255,214,10),14)
F2=ImageFont.truetype(HN,40*K,index=4)
d.text((72*K,350*K),'THE GPU',font=F2,fill=(140,175,255))
bg.resize((1280,720),Image.LANCZOS).save(out,quality=95)
