"""Optimize landing visuals for web: resize to 600px max + JPEG q80."""
from PIL import Image
from pathlib import Path

src = Path(__file__).parent / "visuals"
dst = Path(__file__).parent / "visuals_web"
dst.mkdir(exist_ok=True)

MAX = 600
QUALITY = 82

for f in sorted(src.glob("*.png")):
    im = Image.open(f).convert("RGB")
    im.thumbnail((MAX, MAX), Image.LANCZOS)
    out = dst / (f.stem + ".jpg")
    im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    print(f"{f.name:30s} -> {out.name:30s} {out.stat().st_size//1024}KB")

total = sum(p.stat().st_size for p in dst.glob("*.jpg"))
print(f"\nTotal: {total/1024/1024:.2f} MB across {len(list(dst.glob('*.jpg')))} files")
