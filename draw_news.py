#!/usr/bin/env python3
"""Render the make.fun news-image-20261117 entry: a newspaper front page
summing up Tuesday 17 November 2026 in six stories. Deterministic output:
fixed layout, fixed strings, no timestamps, no randomness.
Draws with Pillow + DejaVu fonts only, no network.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 244, 230)      # off-white paper
INK = (26, 24, 22)           # dark ink
RED = (178, 34, 28)          # masthead red
GREY = (96, 90, 84)          # secondary ink
PANEL = (255, 252, 245)      # panel paper
LINE = (180, 172, 158)       # hairline rules

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("MIDDLE EAST", "US strikes Iran missile site",
     "After Iranian drones hit a US radar in Bahrain"),
    ("UKRAINE", "Kerch Bridge hit again",
     "A road section falls into the strait on day two of drone strikes"),
    ("BUSINESS", "Nvidia tops $115bn revenue",
     "Ousted chief Jensen Huang will not return, board says"),
    ("DIPLOMACY", "Trump heads to Shenzhen",
     "Trilateral talks with Xi and Putin at APEC"),
    ("GAZA", "West urges Israel: open crossings",
     "UK, Australia, Canada, Italy warn of catastrophic winter"),
    ("HEALTH", "Ebola cases pass 11,000",
     "DR Congo outbreak: 5,400 dead in three months"),
]


def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 10], fill=RED)
    f_mast = font("DejaVuSerif-Bold.ttf", 30)
    f_date = font("DejaVuSerif-Bold.ttf", 54)
    f_rule = font("DejaVuSans.ttf", 20)

    t = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(t, font=f_mast)) / 2, 30), t, font=f_mast, fill=RED)

    t = "TUESDAY 17 NOVEMBER 2026"
    d.text(((W - d.textlength(t, font=f_date)) / 2, 78), t, font=f_date, fill=INK)

    d.line([40, 158, W - 40, 158], fill=INK, width=3)
    t = "Six stories from one day around the world"
    d.text(((W - d.textlength(t, font=f_rule)) / 2, 168), t, font=f_rule, fill=GREY)

    # --- Six panels, 2 columns x 3 rows --------------------------------
    x0, y0 = 40, 205
    gap = 20
    pw = (W - 2 * x0 - gap) // 2          # 462
    ph = 238
    f_num = font("DejaVuSans-Bold.ttf", 26)
    f_kick = font("DejaVuSans-Bold.ttf", 21)
    f_head = font("DejaVuSans-Bold.ttf", 33)
    f_sub = font("DejaVuSans.ttf", 22)

    for i, (kicker, headline, sub) in enumerate(STORIES):
        col, row = i % 2, i // 2
        px = x0 + col * (pw + gap)
        py = y0 + row * (ph + gap)

        d.rectangle([px, py, px + pw, py + ph], fill=PANEL, outline=LINE, width=2)
        d.rectangle([px, py, px + pw, py + 5], fill=RED)

        # number badge: red circle, white numeral
        cx, cy, r = px + 36, py + 40, 20
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED)
        num = str(i + 1)
        d.text((cx - d.textlength(num, font=f_num) / 2, cy - 18),
               num, font=f_num, fill=(255, 255, 255))

        # kicker
        d.text((px + 66, py + 22), kicker, font=f_kick, fill=RED)

        # headline, wrapped, max 2 lines
        inner = pw - 40
        lines = wrap(d, headline, f_head, inner)[:2]
        hy = py + 76
        for ln in lines:
            d.text((px + 20, hy), ln, font=f_head, fill=INK)
            hy += 40

        # sub-line, wrapped, max 2 lines
        slines = wrap(d, sub, f_sub, inner)[:2]
        sy = py + 76 + len(lines) * 40 + 12
        for ln in slines:
            d.text((px + 20, sy), ln, font=f_sub, fill=GREY)
            sy += 30

    # --- Footer ---------------------------------------------------------
    fy = y0 + 3 * ph + 2 * gap + 14
    d.line([40, fy, W - 40, fy], fill=INK, width=2)
    f_foot = font("DejaVuSans.ttf", 21)
    t = "One day's world news \u00b7 17 November 2026 \u00b7 make.fun"
    d.text(((W - d.textlength(t, font=f_foot)) / 2, fy + 12),
           t, font=f_foot, fill=INK)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    draw()
