import pyglet
from pyglet import gl

# Velikost okna (v pixelech)
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200  # v pixelech za sekundu
RYCHLOST_PALKY = RYCHLOST * 1.5  # taky v pixelech za sekundu

DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 30

pozice_palek = [VYSKA // 2, VYSKA // 2]  # vertikalni pozice dvou palek
pozice_mice = [0, 0]  # x, y souradnice micku -- nastavene v reset()
rychlost_mice = [0, 0]  # x, y slozky rychlosti micku -- nastavene v reset()
stisknute_klavesy = set()  # sada stisknutych klaves
skore = [0, 0]  # skore dvou hracu


def nakresli_obdelnik(x1, y1, x2, y2):
    """Nakresli obdelnik na dane souradnice

    Nazorny diagram::

         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
    """
    # Tady pouzivam volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # souradnice A
    gl.glVertex2f(int(x1), int(y2))  # souradnice B
    gl.glVertex2f(int(x2), int(y2))  # souradnice C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # souradnice D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuhelniku


def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vybarvi na cerno)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou
    obdelnik = nakresli_obdelnik(0, 0, SIRKA, VYSKA)
    nakresli_obdelnik(  # nechapu tuto definici pozice micku
        pozice_mice[0] - VELIKOST_MICE // 2,  # 0 - 10 se prece dostane do zapornych hodnot...
        pozice_mice[1] - VELIKOST_MICE // 2,
        pozice_mice[0] + VELIKOST_MICE // 2,
        pozice_mice[1] + VELIKOST_MICE // 2,  # proc je tady ta carka? a jinde v () taky
    )
    for x, y in [(0, pozice_palek[0]), (SIRKA, pozice_palek[1])]:  # co je x a co y?
        nakresli_obdelnik(
        x - TLOUSTKA_PALKY,  # co je x tady? prece nemuzu odecitat od tuple
        y - DELKA_PALKY // 2,  # to stejne s y
        x + TLOUSTKA_PALKY,
        y + DELKA_PALKY // 2,
        )

    
window = pyglet.window.Window(width=SIRKA, height=VYSKA)

window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
)

pyglet.app.run()
