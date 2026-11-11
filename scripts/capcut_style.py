"""剪映"系统"字幕样式，2026-11-10 用剪映导出帧逐像素校准。

数值按画面高度的比例给出，任何分辨率都能用：px = 比例 * 画面高度。
校准帧是 2000x1125，误差已降到视频压缩噪声水平（字幕区平均差 5.1，画面其他区域本身噪声 4.2）。
"""
FONT_DIR = "/Applications/VideoFusion-macOS.app/Contents/Resources/Font/SystemFont/"
ZH_FONT = FONT_DIR + "zh-hans.ttf"          # Source Han Sans CN Medium（思源黑体）
EN_FONT = FONT_DIR + "NotoSans-Regular.ttf"  # Noto Sans Regular，剪映渲染时略加粗

ZH_SIZE = 58 / 1125        # 中文字号
EN_SIZE = 58.75 / 1125     # 英文字号
EN_EMBOLDEN = 0.5 / 1125   # 英文加粗（每边描边宽度）
ZH_TOP = 946.5 / 1125      # 中文墨迹顶端位置
EN_TOP = 1019.5 / 1125     # 英文墨迹顶端位置
# 两行都水平居中；无描边、无阴影
WHITE = (255, 255, 255)
HIGHLIGHT = (0, 205, 229)  # 天空蓝 #00CDE5
SUPERSAMPLE = 4            # 4 倍超采样后缩小，抗锯齿和剪映一致
