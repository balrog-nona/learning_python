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
# to nahore jsou konstanty - v prubehu hry se nebudou menit; nize jsou globalni promenne

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
    gl.glColor3f(1, 0, 1)  # nastav barvu kresleni
    obdelnik = nakresli_obdelnik(0, 0, SIRKA, VYSKA)  # nakresleni hraciho pole
    gl.glColor3f(1, 0, 0)  # opet nastavena barva kresleni, aby byly palky videt
    # nasleduje nakresleni micku
    nakresli_obdelnik(
        pozice_mice[0] - VELIKOST_MICE // 2,  # micek je na zacatku z poloviny mimo hraci pole - neni videt cely
        pozice_mice[1] - VELIKOST_MICE // 2,
        pozice_mice[0] + VELIKOST_MICE // 2,
        pozice_mice[1] + VELIKOST_MICE // 2,  # carka je volitelna
    )
    # nasleduje vykresleni palek; vychazi mi z toho, ze jsou taky na zacatku videt jen z poloviny svoji sirky
    for x, y in [(0, pozice_palek[0]), (SIRKA, pozice_palek[1])]:  # nakresleni palek
        nakresli_obdelnik(
        x - TLOUSTKA_PALKY,
        y - DELKA_PALKY // 2,
        x + TLOUSTKA_PALKY,
        y + DELKA_PALKY // 2
        )
    # nakresleni pulici cary
    umisteni = 0
    pauza = 15
    delka = DELKA_PULICI_CARKY
    while umisteni < VYSKA:
        nakresli_obdelnik(
            SIRKA // 2 - 1,
            umisteni,
            SIRKA // 2 + 1,
            delka
        )
        umisteni = umisteni + DELKA_PULICI_CARKY + pauza
        delka = umisteni + DELKA_PULICI_CARKY



"""
k vykresleni palek: x a y znamena x a y z tuple - tyto hodnoty vzniknou, az kdyz se vleze do seznamu a zacina se rozbalovat jednotliva
tuple - zkusit si to na jednoduchem prikladu:
for x, y in [(10, 20), (50, 60)]:
    print(x, y)
Vytvori to souradnice pro obe palky zaroven.
    
Carku za poslednim argumentem nekteri pisou, bo kdyz vkladaji novy radek, tak se nemusi vracet na predchozi a
dopisovat ji tam.
"""
    
window = pyglet.window.Window(width=SIRKA, height=VYSKA)

window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
)

pyglet.app.run()
