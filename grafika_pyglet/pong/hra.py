import pyglet
import random
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
# jak muze mit staticka vec jako souradnice rychlostni aspekt? - rychlost mice
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
        stisknute_klavesy.add(("nahoru", 1))  # cislo reprezentuje palku 0-leva, 1-prava
    if symbol == key.DOWN:
        stisknute_klavesy.add(("dolu", 1))
    if symbol == key.W:
        stisknute_klavesy.add(("nahoru", 0))
    if symbol == key.S:
        stisknute_klavesy.add(("dolu", 0))
    # return stisknute_klavesy - jak to, ze tato fce nic nevraci?


def pusteni_klavesy(symbol, modifikatory):
    if symbol == key.UP:
        stisknute_klavesy.discard(("nahoru", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(("dolu", 1))
    if symbol == key.W:
        stisknute_klavesy.discard(("nahoru", 0))
    if symbol == key.S:
        stisknute_klavesy.discard(("dolu", 0))
    # return stisknute_klavesy - to stejne


def obnov_stav(dt):  # dt je cas posledniho zavolani fce Pygletem
    for cislo_palky in (0, 1):
        # pohyb podle klaves, viz fce stisk_klavesy
        # proc se to nasobi tim dt? ty palky budou po delsi necinnosti desne rychle, ne?
        if ("nahoru", cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] += RYCHLOST_PALKY * dt
        if ("dolu", cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] -= RYCHLOST_PALKY * dt
        """
        meni se v prubehu ta promenna pozice palek? vychozi byla [VYSKA // 2, VYSKA // 2]?
        co se s tou promennou deje v prubehu hry?
        jak to, ze se na staticky prvek, jako jsou souradnice v pozice_palek vaze pohyb? pozice_palek
        totiz ve fci vykresli slouzi k vykresleni toho obdelniku
        """

        # dolni zarazka - kdyz je palka moc dole, nastavime ji na minimum - co se tim mysli?
        if pozice_palek[cislo_palky] < DELKA_PALKY / 2:
            pozice_palek[cislo_palky] = DELKA_PALKY / 2
        # horni zarazka - kdyz je palka moc nahore, nastavime ji na maximum
        if pozice_palek[cislo_palky] > VYSKA - DELKA_PALKY / 2:
            pozice_palek[cislo_palky] = VYSKA - DELKA_PALKY / 2
        #  zarazky jsou nastavene na DELKA_PALKY / 2 - to by palka mela z poloviny zmizet, ne?

    # pohyb micku
    pozice_mice[0] += rychlost_mice[0] * dt
    pozice_mice[1] += rychlost_mice[1] * dt
    # odraz micku od sten
    if pozice_mice[1] < VELIKOST_MICE // 2:  # stejne jako v predchozim - micek by mel z pulky zmizet, ne?
        rychlost_mice[1] = abs(rychlost_mice[1])
    if pozice_mice[1] > VYSKA - VELIKOST_MICE // 2:
        rychlost_mice[1] = -abs(rychlost_mice[1])

    palka_min = pozice_mice[1] - VELIKOST_MICE / 2 - DELKA_PALKY / 2
    palka_max = pozice_mice[1] + VELIKOST_MICE / 2 + DELKA_PALKY / 2
    # odrazeni vlevo
    if pozice_mice[0] < TLOUSTKA_PALKY + VELIKOST_MICE / 2:
        if palka_min < pozice_palek[0] < palka_max:
            # palka je na spravnem miste, odrazime micek
            rychlost_mice[0] = abs(rychlost_mice[0])
        else:
            # palka je jinde, nez ma byt - hrac prohral
            skore[1] += 1
            reset()
    # odrazeni vpravo
    if pozice_mice[0] > SIRKA - (TLOUSTKA_PALKY + VELIKOST_MICE / 2):
        if palka_min < pozice_palek[1] < palka_max:
            rychlost_mice[0] = -abs(rychlost_mice[0])
        else:
            skore[0] += 1
            reset()


def reset():
    pozice_mice[0] = SIRKA // 2
    pozice_mice[1] = VYSKA // 2
    # x-ova rychlost - bud vpravo nebo vlevo
    if random.randint(0, 1):  # ve zkouska.py to taky funguje, ale nechapu to
        rychlost_mice[0] = RYCHLOST
    else:
        rychlost_mice[0] = -RYCHLOST
    # y-ova rychlost uplne nahodna - jak to, ze se to nastavuje jako rychlost, kdyz je to cele o smeru...
    rychlost_mice[1] = random.uniform(-1, 1) * RYCHLOST


reset()

window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
    on_key_press=stisk_klavesy,
    on_key_release=pusteni_klavesy,
)

pyglet.clock.schedule(obnov_stav)
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
