"""
Gerador da arte 8-bit (paleta Dracula) do perfil do GitHub.
Tudo é desenhado com retângulos: nenhuma fonte externa, funciona em qualquer <img> do GitHub.

Uso:  python3 scripts/gen.py      -> regera assets/*.svg
Edite SKILLS / SHEET abaixo para mudar os textos e níveis.
"""
import math, os, random

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

# ---------- paleta Dracula ----------
BG0, BG1, BG2 = "#191a21", "#21222c", "#282a36"
CUR, FG, COM = "#44475a", "#f8f8f2", "#6272a4"
CYAN, GREEN, ORANGE, PINK = "#8be9fd", "#50fa7b", "#ffb86c", "#ff79c6"
PURPLE, RED, YELLOW = "#bd93f9", "#ff5555", "#f1fa8c"

# ---------- fonte bitmap 5x7 ----------
G = {
"A":["01110","10001","10001","11111","10001","10001","10001"],
"B":["11110","10001","10001","11110","10001","10001","11110"],
"C":["01111","10000","10000","10000","10000","10000","01111"],
"D":["11110","10001","10001","10001","10001","10001","11110"],
"E":["11111","10000","10000","11110","10000","10000","11111"],
"F":["11111","10000","10000","11110","10000","10000","10000"],
"G":["01111","10000","10000","10111","10001","10001","01111"],
"H":["10001","10001","10001","11111","10001","10001","10001"],
"I":["11111","00100","00100","00100","00100","00100","11111"],
"J":["00111","00010","00010","00010","10010","10010","01100"],
"K":["10001","10010","10100","11000","10100","10010","10001"],
"L":["10000","10000","10000","10000","10000","10000","11111"],
"M":["10001","11011","10101","10101","10001","10001","10001"],
"N":["10001","11001","10101","10011","10001","10001","10001"],
"O":["01110","10001","10001","10001","10001","10001","01110"],
"P":["11110","10001","10001","11110","10000","10000","10000"],
"Q":["01110","10001","10001","10001","10101","10010","01101"],
"R":["11110","10001","10001","11110","10100","10010","10001"],
"S":["01111","10000","10000","01110","00001","00001","11110"],
"T":["11111","00100","00100","00100","00100","00100","00100"],
"U":["10001","10001","10001","10001","10001","10001","01110"],
"V":["10001","10001","10001","10001","10001","01010","00100"],
"W":["10001","10001","10001","10101","10101","10101","01010"],
"X":["10001","10001","01010","00100","01010","10001","10001"],
"Y":["10001","10001","01010","00100","00100","00100","00100"],
"Z":["11111","00001","00010","00100","01000","10000","11111"],
"0":["01110","10011","10101","10101","10101","11001","01110"],
"1":["00100","01100","00100","00100","00100","00100","01110"],
"2":["01110","10001","00001","00110","01000","10000","11111"],
"3":["11110","00001","00001","01110","00001","00001","11110"],
"4":["00010","00110","01010","10010","11111","00010","00010"],
"5":["11111","10000","11110","00001","00001","10001","01110"],
"6":["00110","01000","10000","11110","10001","10001","01110"],
"7":["11111","00001","00010","00100","01000","01000","01000"],
"8":["01110","10001","10001","01110","10001","10001","01110"],
"9":["01110","10001","10001","01111","00001","00010","01100"],
" ":["00000"]*7,
".":["00000","00000","00000","00000","00000","01100","01100"],
",":["00000","00000","00000","00000","01100","00100","01000"],
":":["00000","01100","01100","00000","01100","01100","00000"],
"-":["00000","00000","00000","11111","00000","00000","00000"],
"_":["00000","00000","00000","00000","00000","00000","11111"],
">":["01000","00100","00010","00001","00010","00100","01000"],
"<":["00010","00100","01000","10000","01000","00100","00010"],
"/":["00001","00010","00010","00100","01000","01000","10000"],
"+":["00000","00100","00100","11111","00100","00100","00000"],
"!":["00100","00100","00100","00100","00100","00000","00100"],
"?":["01110","10001","00001","00110","00100","00000","00100"],
"*":["00000","10101","01110","11111","01110","10101","00000"],
"'":["00100","00100","01000","00000","00000","00000","00000"],
"(":["00010","00100","01000","01000","01000","00100","00010"],
")":["01000","00100","00010","00010","00010","00100","01000"],
"#":["01010","11111","01010","01010","01010","11111","01010"],
"&":["01100","10010","10100","01000","10101","10010","01101"],
"=":["00000","00000","11111","00000","11111","00000","00000"],
"|":["00100","00100","00100","00100","00100","00100","00100"],
"♥":["00000","01010","11111","11111","01110","00100","00000"],
}
# acentos: base + marca em cima (a linha 0 vira o acento, glifo fica comprimido)
G["Ã"] = ["01010"] + ["01110","10001","11111","10001","10001","10001"]
G["Á"] = ["00010"] + ["01110","10001","11111","10001","10001","10001"]
G["É"] = ["00010"] + ["11111","10000","11110","10000","10000","11111"]
G["Í"] = ["00010"] + ["01110","00100","00100","00100","00100","01110"]
G["Ó"] = ["00010"] + ["01110","10001","10001","10001","10001","01110"]
G["Õ"] = ["01010"] + ["01110","10001","10001","10001","10001","01110"]
G["Ç"] = ["01111","10000","10000","10000","01111","00100","01000"]


def runs(cells):
    """cells: set of (x,y) -> path com retângulos horizontais mesclados"""
    rows = {}
    for x, y in cells:
        rows.setdefault(y, []).append(x)
    d = []
    for y in sorted(rows):
        xs = sorted(rows[y]); s = p = xs[0]
        for x in xs[1:] + [None]:
            if x is not None and x == p + 1:
                p = x; continue
            d.append(f"M{s} {y}h{p-s+1}v1h-{p-s+1}z")
            if x is not None: s = p = x
    return "".join(d)


def text_cells(s, x, y, scale=1, spacing=1):
    cells = set(); cx = x
    for ch in s.upper():
        g = G.get(ch, G["?"])
        for r, row in enumerate(g):
            for c, v in enumerate(row):
                if v == "1":
                    for dx in range(scale):
                        for dy in range(scale):
                            cells.add((cx + c*scale + dx, y + r*scale + dy))
        cx += (5 + spacing) * scale
    return cells


def text_w(s, scale=1, spacing=1):
    return len(s) * (5 + spacing) * scale - spacing * scale


def path(cells, color, extra=""):
    return f'<path fill="{color}" d="{runs(cells)}" {extra}/>' if cells else ""


def disc(cx, cy, r):
    return {(x, y) for x in range(cx-r, cx+r+1) for y in range(cy-r, cy+r+1)
            if (x-cx+.5)**2 + (y-cy+.5)**2 <= r*r}


def svg(w, h, cell, body, style, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w*cell}" '
            f'height="{h*cell}" shape-rendering="crispEdges" role="img" aria-label="{title}">'
            f'<title>{title}</title><style>{style}</style>{body}</svg>')

# =====================================================================
# 1) BANNER  (300x100 células, 4px cada = 1200x400)
# =====================================================================
def banner():
    W, H = 300, 100
    rnd = random.Random(7)
    b = []
    # céu em faixas com dithering
    bands = [(0, 30, BG0), (30, 60, BG1), (60, H, BG2)]
    for y0, y1, c in bands:
        b.append(f'<rect x="0" y="{y0}" width="{W}" height="{y1-y0}" fill="{c}"/>')
    for (yy, c) in [(30, BG0), (60, BG1)]:
        dith = {(x, yy + (x % 2)) for x in range(0, W, 2)} | {(x, yy + 2) for x in range(1, W, 4)}
        b.append(path(dith, c))

    # estrelas (3 grupos que piscam em tempos diferentes)
    for i, (col, cls) in enumerate([(FG, "t1"), (PURPLE, "t2"), (CYAN, "t3")]):
        st = set()
        for _ in range(28):
            x, y = rnd.randrange(2, W-2), rnd.randrange(2, 62)
            if (225 < x < 280 and y < 50) or y < 15 or (x < 165 and 20 < y < 60): continue
            st.add((x, y))
            if rnd.random() < .18:
                st |= {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}
        b.append(f'<g class="{cls}">{path(st, col)}</g>')

    # lua
    mx, my, mr = 252, 26, 15
    halo = disc(mx, my, mr+3) - disc(mx, my, mr+1)
    b.append(path({c for c in halo if (c[0]+c[1]) % 2 == 0}, CUR))
    moon = disc(mx, my, mr)
    b.append(path(moon, YELLOW))
    shade = {c for c in moon if (c[0]-mx) - (c[1]-my) > mr*0.55}
    b.append(path(shade, "#d8e070"))
    craters = disc(246, 21, 3) | disc(258, 32, 2) | disc(255, 18, 1) | disc(245, 33, 2)
    b.append(path(craters & moon, "#c9d160"))

    # castelo / skyline em silhueta
    sil, wins = set(), set()
    def block(x0, x1, top, crenel=True, roof=0):
        for x in range(x0, x1):
            for y in range(top, H): sil.add((x, y))
        if crenel:
            for x in range(x0, x1, 2): sil.add((x, top-1))
        if roof:
            midx = (x0 + x1 - 1) / 2
            for k in range(roof):
                half = (x1 - x0) / 2 * (1 - k/roof)
                for x in range(x0, x1):
                    if abs(x - midx) <= half: sil.add((x, top-1-k))
    block(150, 300, 88, crenel=False)
    block(170, 182, 66, roof=9)
    block(182, 214, 76)
    block(196, 206, 58, roof=12)
    block(214, 236, 80)
    block(236, 246, 64, roof=10)
    block(246, 278, 82)
    block(278, 288, 70, roof=8)
    block(120, 150, 92, crenel=False)
    b.append(path(sil, "#14151b"))
    # contorno roxo (luz da lua) do lado direito
    rim = {(x, y) for (x, y) in sil if (x+1, y) not in sil and y < 92}
    b.append(path(rim, CUR))
    for (wx, wy) in [(175, 72), (199, 64), (202, 64), (200, 72), (188, 82), (240, 70),
                     (226, 86), (281, 76), (258, 88), (209, 84)]:
        wins |= {(wx, wy), (wx, wy+1), (wx+1, wy), (wx+1, wy+1)}
    lit_a = {c for c in wins if c[0] % 3 != 0}
    lit_b = wins - lit_a
    b.append(f'<g class="wa">{path(lit_a, ORANGE)}</g>')
    b.append(f'<g class="wb">{path(lit_b, YELLOW)}</g>')
    # chão
    b.append(f'<rect x="0" y="96" width="{W}" height="4" fill="#14151b"/>')
    b.append(path({(x, 96) for x in range(0, W, 3)}, CUR))

    # morcegos (2 frames)
    up = ["#.......#", "##.....##", "###.#.###", ".#######.", "...###...", "....#...."]
    dn = [".........", "...#.#...", ".#######.", "#########", "#..###..#", "....#...."]
    def bat(frame, ox, oy):
        return {(ox+c, oy+r) for r, row in enumerate(frame) for c, v in enumerate(row) if v == "#"}
    for i, (sx, sy, dur, delay) in enumerate([(-20, 40, 18, 0), (-20, 52, 24, -9), (-20, 34, 30, -20)]):
        b.append(f'<g class="fly" style="animation-duration:{dur}s;animation-delay:{delay}s">'
                 f'<g class="fa">{path(bat(up, sx, sy), "#0e0f13")}{path({(sx+3, sy+3), (sx+5, sy+3)}, RED)}</g>'
                 f'<g class="fb">{path(bat(dn, sx, sy), "#0e0f13")}{path({(sx+3, sy+3), (sx+5, sy+3)}, RED)}</g></g>')

    # HUD estilo arcade
    b.append(path(text_cells("1UP", 8, 5), RED))
    b.append(path(text_cells("STAGE 02", 30, 5), FG))
    b.append(path(text_cells("HI-SCORE", 122, 5), RED))
    b.append(path(text_cells("2026", 174, 5), FG))

    # título
    name = "CATARINA"; name2 = "COSTA"
    tx, ty = 12, 24
    shadow = text_cells(name, tx+1, ty+1, 3) | text_cells(name2, tx+1, ty+25, 3)
    b.append(path(shadow, "#4b2d63"))
    b.append(path(text_cells(name, tx, ty, 3), PINK))
    b.append(path(text_cells(name2, tx, ty+24, 3), PURPLE))
    # brilho no topo das letras
    hl = {(x, y) for (x, y) in text_cells(name, tx, ty, 3) if (x, y-1) not in text_cells(name, tx, ty, 3)}
    b.append(path(hl, "#ffb3e0"))

    b.append(path(text_cells("DEV QUE SE APAIXONOU POR IA", 12, 74), CYAN))
    b.append(path(text_cells("> WEB / PYTHON / AGENTES / RAG", 12, 85), GREEN))
    b.append(f'<rect class="cur" x="{12 + text_w("> WEB / PYTHON / AGENTES / RAG") + 2}" y="85" width="5" height="7" fill="{GREEN}"/>')

    style = (
        "@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}"
        ".t1{animation:tw 3s steps(3) infinite}.t2{animation:tw 4.5s steps(3) infinite -1s}"
        ".t3{animation:tw 2.2s steps(2) infinite -.5s}"
        "@keyframes fl{from{transform:translate(0,0)}25%{transform:translate(85px,-6px)}"
        "50%{transform:translate(170px,3px)}75%{transform:translate(255px,-4px)}to{transform:translate(345px,0)}}"
        ".fly{animation:fl 18s steps(120) infinite}"
        "@keyframes fa{0%,49%{opacity:1}50%,100%{opacity:0}}@keyframes fb{0%,49%{opacity:0}50%,100%{opacity:1}}"
        ".fa{animation:fa .5s infinite}.fb{animation:fb .5s infinite}"
        "@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:0}}.cur{animation:bl 1s infinite}"
        "@keyframes fk{0%,100%{opacity:1}40%{opacity:.55}45%{opacity:1}70%{opacity:.8}}"
        ".wa{animation:fk 2.7s steps(4) infinite}.wb{animation:fk 3.9s steps(4) infinite -1.3s}"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
    )
    return svg(W, H, 4, "".join(b), style, "Catarina Costa - dev que se apaixonou por IA")

# =====================================================================
# 2) FICHA DE PERSONAGEM (RPG)
# =====================================================================
SHEET = [
    ("CLASSE", "DEV + IA GENERATIVA", PINK),
    ("GUILDA", "IBM BRASIL", CYAN),
    ("BASE", "CAMPINAS - SP", FG),
    ("ESCOLA", "FIAP / ADS 2026", FG),
    ("ESPECIAL", "ACHAR A CAUSA RAIZ", YELLOW),
]
SKILLS = [  # nome, nível 0-10, cor
    ("HTML / CSS / JS", 7, ORANGE),
    ("PYTHON", 8, GREEN),
    ("SQL / PL-SQL", 6, CYAN),
    ("AGENTES DE IA", 8, PINK),
    ("RAG / PROMPTS", 8, PURPLE),
    ("RCA POR TRACES", 9, RED),
    ("VLM / OCR", 7, YELLOW),
]
def sheet():
    W, H = 280, 172
    b = [f'<rect width="{W}" height="{H}" fill="{BG0}"/>']
    # janela estilo RPG com borda dupla
    def frame(x, y, w, h, title, col):
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{BG2}"/>')
        border = set()
        for i in range(w):
            border |= {(x+i, y), (x+i, y+h-1)}
        for j in range(h):
            border |= {(x, y+j), (x+w-1, y+j)}
        inner = set()
        for i in range(2, w-2):
            inner |= {(x+i, y+2), (x+i, y+h-3)}
        for j in range(2, h-2):
            inner |= {(x+2, y+j), (x+w-3, y+j)}
        b.append(path(border, col)); b.append(path(inner, CUR))
        tw = text_w(title)
        b.append(f'<rect x="{x+6}" y="{y-3}" width="{tw+4}" height="9" fill="{BG0}"/>')
        b.append(path(text_cells(title, x+8, y-2), col))

    frame(4, 6, 132, 162, "STATUS", PINK)
    frame(142, 6, 134, 162, "SKILLS", PURPLE)

    # retrato: emblema de morcego + lua
    em = disc(26, 30, 10)
    b.append(path(em, CUR))
    b.append(path(disc(26, 30, 7), YELLOW))
    batt = ["#.........#", "##.#...#.##", "###########", ".#########.", "...#####...", "....###....", ".....#....."]
    bc = {(20+c, 26+r) for r, row in enumerate(batt) for c, v in enumerate(row) if v == "#"}
    b.append(path(bc, BG0))
    b.append(path(text_cells("CATARINA", 42, 20), FG))
    b.append(path(text_cells("LV.2026", 42, 30), GREEN))
    # barras HP/MP
    def bar(x, y, w, frac, col, label, cls=""):
        b.append(path(text_cells(label, x, y), COM))
        bx = x + 14
        b.append(f'<rect x="{bx}" y="{y}" width="{w}" height="7" fill="{BG0}"/>')
        b.append(f'<rect x="{bx+1}" y="{y+1}" width="{w-2}" height="5" fill="{CUR}"/>')
        fw = round((w-2)*frac)
        b.append(f'<rect class="{cls}" x="{bx+1}" y="{y+1}" width="{fw}" height="5" fill="{col}" style="transform-origin:{bx+1}px 0"/>')
        b.append(f'<rect x="{bx+1}" y="{y+1}" width="{fw}" height="1" fill="#ffffff" opacity=".35"/>')
    bar(12, 46, 60, 1, GREEN, "HP", "grow")
    bar(12, 56, 60, .85, CYAN, "MP", "grow")
    b.append(path(text_cells("CAFE", 92, 46), COM))
    b.append(path(text_cells("FULL", 92, 56), COM))

    y = 70
    for k, v, col in SHEET:
        b.append(path(text_cells(k, 12, y), COM))
        b.append(path(text_cells(v, 12, y + 9), col))
        y += 19
    # skills
    y = 18
    for name, lvl, col in SKILLS:
        b.append(path(text_cells(name, 150, y), FG))
        y += 9
        for i in range(10):
            x = 150 + i*12
            filled = i < lvl
            blk = {(x+dx, y+dy) for dx in range(10) for dy in range(5)}
            b.append(f'<g class="pip" style="animation-delay:{i*0.08 + (y/100):.2f}s">'
                     f'{path(blk, col if filled else CUR)}'
                     f'{path({(x+dx, y) for dx in range(10)}, "#ffffff", 'opacity=".3"') if filled else ""}</g>')
        y += 12
    style = ("@keyframes gr{from{transform:scaleX(0)}to{transform:scaleX(1)}}"
             ".grow{animation:gr 1.2s steps(12) both}"
             "@keyframes pp{from{opacity:0}to{opacity:1}}.pip{animation:pp .2s steps(1) both}"
             "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
    return svg(W, H, 3, "".join(b), style, "Ficha de personagem: status e skills")

# =====================================================================
# 3) divisória e rodapé
# =====================================================================
def divider(label, col):
    W, H = 280, 13
    b = []
    tw = text_w(label)
    x0 = (W - tw) // 2
    line = set()
    for x in range(0, W):
        if x0 - 6 <= x <= x0 + tw + 5: continue
        if x % 4 in (0, 1): line.add((x, 6))
    b.append(path(line, CUR))
    for cx in (x0-4, x0+tw+3):
        b.append(path({(cx, 5), (cx-1, 6), (cx, 6), (cx+1, 6), (cx, 7)}, col))
    b.append(path(text_cells(label, x0, 3), col))
    return svg(W, H, 3, "".join(b), "", label)


def footer():
    W, H = 280, 27
    b = []
    t1 = "GAME SAVED"
    b.append(path(text_cells(t1, (W - text_w(t1, 2)) // 2, 1, 2), GREEN))
    t2 = "OBRIGADA POR JOGAR!  CONTINUE? 9"
    b.append(f'<g class="bl">{path(text_cells(t2, (W - text_w(t2)) // 2, 19), PINK)}</g>')
    style = "@keyframes bl{0%,59%{opacity:1}60%,100%{opacity:0}}.bl{animation:bl 1.4s infinite}"
    return svg(W, H, 3, "".join(b), style, "Game saved")


# =====================================================================
# 4) WORLD MAP: a jornada dev -> IA
# =====================================================================
WORLDS = [  # (rótulo no bloco, título, linha 2, linha 3, cor, estado)
    ("1", "WEB",     "HTML CSS", "JS",      ORANGE, "CLEAR"),
    ("2", "BACKEND", "PYTHON",   "SQL",     CYAN,   "CLEAR"),
    ("3", "DADOS",   "3X IBM",   "2025",    GREEN,  "CLEAR"),
    ("4", "IA GEN",  "IBM",      "2026",    PINK,   "AGORA"),
    ("?", "PROXIMA", "FASE",     "...",     CUR,    ""),
]
def worldmap():
    W, H = 280, 96
    b = [f'<rect width="{W}" height="{H}" fill="{BG0}"/>']
    x, y, w, h = 4, 6, 272, 86
    b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{BG2}"/>')
    border = {(x+i, y) for i in range(w)} | {(x+i, y+h-1) for i in range(w)} \
           | {(x, y+j) for j in range(h)} | {(x+w-1, y+j) for j in range(h)}
    inner = {(x+i, y+2) for i in range(2, w-2)} | {(x+i, y+h-3) for i in range(2, w-2)} \
          | {(x+2, y+j) for j in range(2, h-2)} | {(x+w-3, y+j) for j in range(2, h-2)}
    b.append(path(border, PURPLE)); b.append(path(inner, CUR))
    title = "MINHA JORNADA"
    b.append(f'<rect x="{x+6}" y="{y-3}" width="{text_w(title)+4}" height="9" fill="{BG0}"/>')
    b.append(path(text_cells(title, x+8, y-2), PURPLE))

    xs = [34, 86, 138, 190, 244]
    ys = [40, 33, 41, 33, 40]
    # trilha pontilhada entre as fases (colorida até a fase atual)
    for i in range(len(xs)-1):
        x0, y0, x1, y1 = xs[i], ys[i], xs[i+1], ys[i+1]
        n = int(max(abs(x1-x0), abs(y1-y0)))
        dots = set()
        for k in range(10, n-9, 4):
            t = k / n
            px, py = round(x0 + (x1-x0)*t), round(y0 + (y1-y0)*t)
            dots |= {(px, py), (px+1, py), (px, py+1), (px+1, py+1)}
        col = WORLDS[i+1][4] if WORLDS[i+1][5] else CUR
        cls = ' class="nx"' if not WORLDS[i+1][5] else ""
        b.append(f'<g{cls}>{path(dots, col)}</g>')
    for (lab, t1, t2, t3, col, st), cx, cy in zip(WORLDS, xs, ys):
        s = 15; x0, y0 = cx - 7, cy - 7
        blk = {(x0+i, y0+j) for i in range(s) for j in range(s)}
        blk -= {(x0, y0), (x0+s-1, y0), (x0, y0+s-1), (x0+s-1, y0+s-1)}
        sh = {(px+1, py+1) for (px, py) in blk}
        b.append(path(sh - blk, "#0e0f13"))
        g = path(blk, col)
        g += path({(px, py) for (px, py) in blk if py == y0+1 or px == x0+1}, "#ffffff", 'opacity=".35"')
        g += path({(px, py) for (px, py) in blk if py == y0+s-2 or px == x0+s-2}, "#000000", 'opacity=".3"')
        g += path(text_cells(lab, cx - 2, cy - 3), BG0 if st else FG)
        if st == "AGORA":
            ring = {(x0-2+i, y0-2) for i in range(s+4)} | {(x0-2+i, y0+s+1) for i in range(s+4)} \
                 | {(x0-2, y0-2+j) for j in range(s+4)} | {(x0+s+1, y0-2+j) for j in range(s+4)}
            g += f'<g class="pulse">{path(ring, col)}</g>'
        cls = ' class="nx"' if not st else ""
        b.append(f'<g{cls}>{g}</g>')
        if st:
            tag = f'<g class="bl">' if st == "AGORA" else "<g>"
            b.append(tag + path(text_cells(st, cx - text_w(st)//2, cy - 19), GREEN if st == "CLEAR" else col) + "</g>")
        for k, (txt, c) in enumerate([(t1, col if st else COM), (t2, FG if st else COM), (t3, COM)]):
            b.append(path(text_cells(txt, cx - text_w(txt)//2, 56 + k*9), c))
    style = ("@keyframes bl{0%,59%{opacity:1}60%,100%{opacity:0}}.bl{animation:bl 1s infinite}"
             "@keyframes pu{0%,100%{opacity:1}50%{opacity:.2}}.pulse{animation:pu 1.2s steps(3) infinite}"
             "@keyframes nx{0%,100%{opacity:.35}50%{opacity:1}}.nx{animation:nx 2.4s steps(4) infinite}"
             "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
    return svg(W, H, 3, "".join(b), style, "Minha jornada: web, backend, dados, IA generativa")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    files = {
        "banner.svg": banner(),
        "status.svg": sheet(),
        "footer.svg": footer(),
        "worldmap.svg": worldmap(),
        "div-origem.svg": divider("ORIGIN STORY", ORANGE),
        "div-boss.svg": divider("BOSS FIGHTS", RED),
        "div-inv.svg": divider("INVENTARIO", YELLOW),
        "div-save.svg": divider("SAVE FILES", PURPLE),
        "div-map.svg": divider("MAPA DE CONTRIBUICOES", GREEN),
        "div-pm.svg": divider("MANDAR MENSAGEM", CYAN),
    }
    for n, s in files.items():
        with open(os.path.join(OUT, n), "w") as f: f.write(s)
        print(n, len(s)//1024, "KB")
