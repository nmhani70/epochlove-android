from PIL import Image, ImageDraw
import os

BASE = os.path.expanduser("~/epochlove-android/app/src/main/res")
SIZES = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (5, 3, 15, 255))
    draw = ImageDraw.Draw(img)
    r = size // 8
    draw.ellipse([r, r, size - r, size - r], fill=(255, 45, 120, 255))
    draw.ellipse([r + size//8, r, size - r, size - r - size//8], fill=(168, 85, 247, 255))
    cx, cy = size // 2, size // 2
    hs = size // 3
    draw.ellipse([cx - hs//2, cy - hs//3, cx, cy + hs//6], fill=(255, 255, 255, 255))
    draw.ellipse([cx, cy - hs//3, cx + hs//2, cy + hs//6], fill=(255, 255, 255, 255))
    draw.polygon([(cx - hs//2, cy), (cx + hs//2, cy), (cx, cy + hs//2)], fill=(255, 255, 255, 255))
    img.save(path, 'PNG')

for folder, size in SIZES.items():
    d = os.path.join(BASE, folder)
    os.makedirs(d, exist_ok=True)
    make_icon(size, os.path.join(d, "ic_launcher.png"))
    print("Created " + folder + "/ic_launcher.png")
