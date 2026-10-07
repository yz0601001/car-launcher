# 生成车机桌面 iOS 图标 (180x180)
from PIL import Image, ImageDraw

S = 180
img = Image.new("RGB", (S, S), "#0a0c10")
d = ImageDraw.Draw(img)

# 背景微妙渐变（上下暗角）
for y in range(S):
    t = y / S
    r = int(10 + 18 * (1 - t))
    g = int(12 + 20 * (1 - t))
    b = int(16 + 28 * (1 - t))
    d.line([(0, y), (S, y)], fill=(r, g, b))

cx, cy = S / 2, S / 2
R = 58          # 方向盘外圈半径
W = 15          # 外圈宽度
ACCENT = (255, 159, 10)

# 外圈
d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=ACCENT, width=W)

# 三辐条
d.rectangle([cx - R + 4, cy - 6, cx + R - 4, cy + 6], fill=ACCENT)  # 横辐
d.rectangle([cx - 6, cy, cx + 6, cy + R - 4], fill=ACCENT)          # 下辐

# 中心轮毂
d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(10, 12, 16), outline=ACCENT, width=5)

img.save(r"D:\Claude code\car-launcher\icon.png")
print("icon.png 已生成")
