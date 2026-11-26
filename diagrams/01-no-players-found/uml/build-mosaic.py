# Combines the use case diagrams into one mosaic: uc-devices.svg
# Run from diagrams/<level>/ after: plantuml -tsvg uml/*.puml
# Each tile is (diagram name, column, row, columns spanned).
import re
tiles_spec = [("uc-leo-pc", 0, 0, 1), ("uc-mia-pc", 1, 0, 1)]
COLS, ROWS = 2, 1
TW, TH, PAD = 420, 260, 16
tiles = []
for name, col, row, span in tiles_spec:
    s = open(f"uml/{name}.svg").read()
    s = re.sub(r"<\?[^>]*\?>", "", s)
    m = re.search(r"<svg\b[^>]*>", s)
    vx, vy, vw, vh = map(float, re.search(r'viewBox="([^"]+)"', m.group(0)).group(1).split())
    body = s[m.end():s.rindex("</svg>")]
    body = re.sub(r'id="([^"]+)"', lambda g: f'id="{name}-{g.group(1)}"', body)
    body = re.sub(r'url\(#([^)]+)\)', lambda g: f'url(#{name}-{g.group(1)})', body)
    body = re.sub(r'href="#([^"]+)"', lambda g: f'href="#{name}-{g.group(1)}"', body)
    cw = TW * span
    scale = min(1.0, (cw - 2*PAD) / vw, (TH - 2*PAD) / vh)
    w, h = vw * scale, vh * scale
    x = col * TW + (cw - w) / 2
    y = row * TH + (TH - h) / 2
    tiles.append(f'  <svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="{vx} {vy} {vw} {vh}">{body}</svg>')
W, H = TW * COLS, TH * ROWS
lines = "".join(f'    <line x1="{TW*c}" y1="0" x2="{TW*c}" y2="{H}"/>\n' for c in range(1, COLS))
out = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
       f'  <rect width="{W}" height="{H}" fill="#FFFFFF"/>\n' + "\n".join(tiles) + "\n"
       f'  <g stroke="#000000" stroke-width="2" fill="none">\n    <rect x="1" y="1" width="{W-2}" height="{H-2}"/>\n' + lines + '  </g>\n</svg>\n')
open("uc-devices.svg", "w").write(out)
