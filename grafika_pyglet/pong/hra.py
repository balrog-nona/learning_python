import pyglet
from pyglet import gl
from pyglet.window import key

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


def nakresli_text(text, x, y, pozice_x):
    """Nakresli dany text na danou pozici

    Argument 'pozice_x' muze byt 'left' nebo 'right' udava, na kterou stranu bude text zarovnany
    """
    napis = pyglet.text.Label(
        text,
        font_size=VELIKOST_FONTU,
        x=x, y=y, anchor_x=pozice_x
    )
    napis.draw()


def vykresli():
    # vykresli stav hry
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vybarvi na cerno)
    gl.glColor3f(1, 0, 1)  # nastav barvu kresleni pro palky, micek a pulici caru

    # nasleduje nakresleni micku - je na zacatku z poloviny mimo hraci pole - neni videt cely
    nakresli_obdelnik(
        pozice_mice[0] - VELIKOST_MICE // 2,
        pozice_mice[1] - VELIKOST_MICE // 2,
        pozice_mice[0] + VELIKOST_MICE // 2,
        pozice_mice[1] + VELIKOST_MICE // 2,  # carka je volitelna
    )

    # nasleduje vykresleni palek; vychazi mi z toho, ze jsou taky na zacatku videt jen z poloviny svoji sirky
    for x, y in [(0, pozice_palek[0]), (SIRKA, pozice_palek[1])]:
        nakresli_obdelnik(
            x - TLOUSTKA_PALKY,
            y - DELKA_PALKY // 2,
            x + TLOUSTKA_PALKY,
            y + DELKA_PALKY // 2
        )

    # nasleduje vykresleni pulici cary - muj vytvor, oficialni reseni je elegantnejsi
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

    # nasleduje vykresleni skore - oboje jsou zcela videt, takze je nejde nakreslit naraz
    nakresli_text(
        str(skore[0]),
        x=ODSAZENI_TEXTU,
        y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
        pozice_x="left"
    )
    nakresli_text(
        str(skore[1]),
        x=SIRKA - ODSAZENI_TEXTU,
        y=VYSKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
        pozice_x="right"
    )


window = pyglet.window.Window(width=SIRKA, height=VYSKA)


def stisk_klavesy(symbol, modifikatory):
    if symbol == key.UP:
        stisknute_klavesy.add("nahoru", 1),
    elif symbol == key.DOWN:
        stisknute_klavesy.add("dolu", 1),
    elif symbol == key.W:
        stisknute_klavesy.add("nahoru", 0),
    elif symbol == key.S:
        stisknute_klavesy.add("dolu", 0)


def pusteni_klavesy(symbol, modifikatory):


window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
    on_key_press=stisk_klavesy,
    on_key_release=pusteni_klavesy,
)

pyglet.app.run()


"""
k vykresleni palek: x a y znamena x a y z tuple - tyto hodnoty vzniknou, az kdyz se vleze do seznamu a zacina se 
rozbalovat jednotliva tuple - zkusit si to na jednoduchem prikladu:
for x, y in [(10, 20), (50, 60)]:
    print(x, y)
Vytvori to souradnice pro obe palky zaroven.

Carku za poslednim argumentem nekteri pisou, bo kdyz vkladaji novy radek, tak se nemusi vracet na predchozi a
dopisovat ji tam.
"""
