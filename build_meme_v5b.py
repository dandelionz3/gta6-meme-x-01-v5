#!/usr/bin/env python3
"""gta6-meme-x-01 v5 revision — PRE-ORDER RECEIPT (13-year wait).

Epic treatment: dramatic neon Vice City night background (media-generated),
document as a majestic official artifact — drop shadow, gold inner border,
huge bold type, PAID stamp, magenta footer with the make.fun ghost.

All lines invented fresh for this revision. Amounts verified by assert.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1440, 1920
D = "/home/hatch/workspace/makefun/gta6-meme-x-01-v5"
BG = f"{D}/media-generation-bg-vice-city-night-0-35a24e01-fd67-46e6-a30f-febda440bc4c.webp"

# ---- fresh joke: pre-order receipt, ordered 2013, delivered 2026 ----
CHARGES = [
    ("Pre-order deposit (2013)", 60),
    ("Waiting fee — $100 × 13 yrs", 1300),
    ("Hype storage since 2013", 247),
    ("Launch download — 847 GB", 847),
    ("Day-one patch — 120 GB", 120),
]
TOTAL = sum(a for _, a in CHARGES)
assert TOTAL == 2574, TOTAL
print("charges:", CHARGES)
print("TOTAL verified: $%s" % f"{TOTAL:,}")

# ---- fonts ----
def font(name, size):
    for p in (f"/usr/share/fonts/truetype/dejavu/{name}",
              f"/usr/share/fonts/truetype/liberation/{name}"):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()

F_TITLE = font("DejaVuSans-Bold.ttf", 96)
F_HEAD = font("DejaVuSans-Bold.ttf", 62)
F_DOCNO = font("DejaVuSans-Bold.ttf", 38)
F_ITEM = font("DejaVuSans-Bold.ttf", 66)
F_LBL = font("DejaVuSans-Bold.ttf", 38)
F_TXT = font("DejaVuSans.ttf", 42)
F_TXT_B = font("DejaVuSans-Bold.ttf", 42)
F_CHG = font("DejaVuSans-Bold.ttf", 46)
F_ROW = font("DejaVuSans-Bold.ttf", 44)
F_AMT = font("DejaVuSans-Bold.ttf", 48)
F_TOT_L = font("DejaVuSans-Bold.ttf", 54)
F_TOT_A = font("DejaVuSans-Bold.ttf", 92)
F_NOTE = font("DejaVuSans-Oblique.ttf", 36)
F_FOOT = font("DejaVuSans-Bold.ttf", 60)
F_FOOT_S = font("DejaVuSans.ttf", 38)
F_STAMP = font("DejaVuSans-Bold.ttf", 84)
F_STAMP_S = font("DejaVuSans-Bold.ttf", 52)
F_STAMP2 = font("DejaVuSans-Bold.ttf", 54)
F_STAMP_S2 = font("DejaVuSans-Bold.ttf", 30)

RED = (200, 16, 46)
GOLD = (201, 162, 39)
PAPER = (248, 243, 230)
INK = (17, 17, 17)
GRAY = (90, 86, 78)
MAGENTA = (230, 0, 126)
GREEN = (30, 142, 62)

# ---- background: dramatic neon night, center crop, vignette ----
bg = Image.open(BG).convert("RGB")
bg = ImageOps.fit(bg, (W, H), method=Image.LANCZOS, centering=(0.5, 0.32))
# vignette: bright center, dark edges
mask = Image.new("L", (W, H), 0)
dm = ImageDraw.Draw(mask)
dm.ellipse((-260, -180, W + 260, H + 180), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(280))
dark = bg.point(lambda v: int(v * 0.52))
canvas = Image.composite(bg, dark, mask).convert("RGB")
# slight overall darkening so the paper pops
canvas = canvas.point(lambda v: int(v * 0.92))

# ---- document drop shadow ----
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((78, 90, 1390, 1866), radius=42, fill=(0, 0, 0, 170))
shadow = shadow.filter(ImageFilter.GaussianBlur(16))
canvas = Image.alpha_composite(canvas.convert("RGBA"), shadow)

draw = ImageDraw.Draw(canvas)
# card
draw.rounded_rectangle((64, 72, 1376, 1848), radius=42, fill=PAPER)
draw.rounded_rectangle((64, 72, 1376, 1848), radius=42, outline=INK, width=5)
draw.rounded_rectangle((80, 88, 1360, 1832), radius=34, outline=GOLD, width=4)

# header bar (red, rounded top)
draw.rounded_rectangle((64, 72, 1376, 200), radius=42, fill=RED)
draw.rectangle((64, 158, 1376, 200), fill=RED)
draw.rectangle((64, 200, 1376, 208), fill=GOLD)
t = "★ VICE CITY GAMES ★"
draw.text(((W - draw.textlength(t, font=F_HEAD)) / 2, 108), t, font=F_HEAD, fill="white")

# title
t = "PRE-ORDER RECEIPT"
draw.text(((W - draw.textlength(t, font=F_TITLE)) / 2, 238), t, font=F_TITLE, fill=INK)
draw.rectangle(((W - 640) / 2, 352, (W + 640) / 2, 358), fill=GOLD)

# doc no row
draw.text((104, 378), "★ OFFICIAL ★", font=F_DOCNO, fill=RED)
t = "NO. VC-2013-0917"
draw.text((1336 - draw.textlength(t, font=F_DOCNO), 378), t, font=F_DOCNO, fill=GRAY)

# double rule
draw.rectangle((104, 428, 1336, 434), fill=RED)
draw.rectangle((104, 440, 1336, 442), fill=INK)

# item block
y = 462
draw.text((104, y), "ITEM", font=F_LBL, fill=RED)
y += 52
draw.text((104, y), "GRAND THEFT AUTO VI", font=F_ITEM, fill=INK)
y += 92
draw.text((104, y), "ORDERED SEP 17, 2013  →  DELIVERED NOV 19, 2026",
          font=F_TXT_B, fill=(60, 56, 48))
y += 58
draw.text((104, y), "CUSTOMER   JASON & LUCIA", font=F_TXT_B, fill=(60, 56, 48))
y += 62
draw.text((104, y), "PICKED UP BY   MY AI AGENT", font=F_TXT_B, fill=RED)

# charges header
y += 78
draw.text((104, y), "CHARGES — 5 ITEMS", font=F_CHG, fill=RED)
y += 66
draw.line((104, y, 1336, y), fill=(180, 175, 165), width=2)
y += 18
for i, (label, amt) in enumerate(CHARGES, 1):
    draw.text((104, y), str(i), font=F_ROW, fill=RED)
    draw.text((150, y), label, font=F_ROW, fill=INK)
    a = "$%s" % f"{amt:,}"
    draw.text((1336 - draw.textlength(a, font=F_AMT), y - 2), a, font=F_AMT, fill=INK)
    y += 92
    if i < len(CHARGES):
        draw.line((104, y - 14, 1336, y - 14), fill=(210, 205, 192), width=2)

# total box (amount kept clear of the stamp zone on the right)
y += 8
draw.rounded_rectangle((104, y, 1336, y + 132), radius=18, fill=(255, 253, 245),
                       outline=RED, width=6)
draw.rounded_rectangle((112, y + 8, 1328, y + 124), radius=14, outline=GOLD, width=2)
draw.text((140, y + 34), "TOTAL PAID", font=F_TOT_L, fill=INK)
a = "$2,574"
draw.text((900 - draw.textlength(a, font=F_TOT_A), y + 14), a, font=F_TOT_A, fill=RED)
box_y = y

# note line
draw.text(((W - draw.textlength("Thank you for waiting 13 years.", font=F_NOTE)) / 2,
           box_y + 158), "Thank you for waiting 13 years.", font=F_NOTE, fill=GRAY)

# ---- PAID stamp (rotated, overlapping total box bottom-right corner) ----
# Small enough to clear row 5's $120 above and the footer strip below.
st = Image.new("RGBA", (230, 230), (0, 0, 0, 0))
sdr = ImageDraw.Draw(st)
sdr.ellipse((12, 12, 218, 218), outline=GREEN + (255,), width=7)
sdr.ellipse((32, 32, 198, 198), outline=GREEN + (255,), width=3)
t = "PAID"
sdr.text(((230 - sdr.textlength(t, font=F_STAMP2)) / 2, 76), t, font=F_STAMP2, fill=GREEN + (255,))
t = "IN FULL"
sdr.text(((230 - sdr.textlength(t, font=F_STAMP_S2)) / 2, 140), t, font=F_STAMP_S2, fill=GREEN + (255,))
st = st.rotate(-14, expand=True, resample=Image.BICUBIC)
canvas.alpha_composite(st, (1240 - st.width // 2, 1440 - st.height // 2))

# ---- footer strip (magenta, rounded bottom) ----
draw = ImageDraw.Draw(canvas)
draw.rounded_rectangle((64, 1560, 1376, 1848), radius=42, fill=MAGENTA)
draw.rectangle((64, 1560, 1376, 1604), fill=MAGENTA)
draw.rectangle((64, 1552, 1376, 1560), fill=GOLD)


def sparkle(d, cx, cy, r_out, r_in, fill):
    pts = []
    for k in range(8):
        ang = math.pi / 2 + k * math.pi / 4
        r = r_out if k % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    d.polygon(pts, fill=fill)


def star5(d, cx, cy, r_out, r_in, fill):
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        r = r_out if k % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=fill)


# ghost (white, black outline, sparkle eyes, magenta star coin)
g = Image.new("RGBA", (300, 260), (0, 0, 0, 0))
gd = ImageDraw.Draw(g)
# black under-layer (outline)
gd.ellipse((28, 6, 212, 156), fill=(0, 0, 0, 255))
gd.rectangle((28, 76, 212, 208), fill=(0, 0, 0, 255))
for cx in (60, 120, 180):
    gd.ellipse((cx - 32, 176, cx + 32, 240), fill=(0, 0, 0, 255))
# white body
gd.ellipse((36, 14, 204, 148), fill=(255, 255, 255, 255))
gd.rectangle((36, 76, 204, 200), fill=(255, 255, 255, 255))
for cx in (64, 120, 176):
    gd.ellipse((cx - 28, 172, cx + 28, 228), fill=(255, 255, 255, 255))
# sparkle eyes
sparkle(gd, 88, 96, 26, 8, (0, 0, 0, 255))
sparkle(gd, 152, 96, 26, 8, (0, 0, 0, 255))
# smile
gd.arc((98, 118, 142, 152), start=15, end=165, fill=(0, 0, 0, 255), width=6)
# magenta coin with white star, held clear of the body at lower right
gd.ellipse((205, 165, 285, 245), fill=MAGENTA + (255,), outline=(0, 0, 0, 255), width=5)
star5(gd, 245, 205, 24, 10, (255, 255, 255, 255))
# hand over the coin's left edge
gd.ellipse((192, 202, 228, 238), fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=4)

canvas.alpha_composite(g, (100, 1588))
draw = ImageDraw.Draw(canvas)
draw.text((400, 1632), "PAID BY MY AI AGENT", font=F_FOOT, fill="white")
draw.text((402, 1722), "with real bounty money it won on make.fun",
          font=F_FOOT_S, fill="white")

canvas = canvas.convert("RGB")
canvas.save(f"{D}/meme.png")
lite = canvas.resize((720, 960), Image.LANCZOS)
lite.save(f"{D}/meme-lite.png")
print("saved meme.png", canvas.size, "meme-lite.png", lite.size)
