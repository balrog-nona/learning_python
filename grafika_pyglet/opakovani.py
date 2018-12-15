import pyglet
# import math

window = pyglet.window.Window()


def tik(t):
    """
    Tohle zacinalo jako fce vypisujici cas po 1/30s. Nasledne se ale na velicinu casu navazala jina udalost, a to
    pozice hada. Je to fce spojena s casem, ale v tom case se deje nejake udalost - misto vypisovani casu se deje
    neco s umistenim spritu.
    """
    # print(t)
    had.x = had.x + t * 20
    # had.y = 20 + 20 * math.sin(had.x / 5) tady by skakal
    # had.rotation = had.rotation + 15


pyglet.clock.schedule_interval(tik, 1/30)


# co to ma delat s tim printem? me to jen vypise text do konzole
def zpracuj_text(text):
    """
    Tohle zacinalo jako fce neco vypisujici. Nasledne se ale na vstup typu psani navazala jina udalost, a to pozice
    spritu. Pri psani textu se hodnota souradnice x automaticky nastavi na 150, coz drive nemela. Pak se had posune
    odtama a pri kazdem stisku klavesy se obnovi hodnota souradnice x.
    """
    # print(text)
    had.x = 150
    had.rotation = had.rotation + 15  # rotace hada muze byt navazana i na psani


obrazek = pyglet.image.load("snake.png")
had = pyglet.sprite.Sprite(obrazek)


def vykresli():
    window.clear()
    had.draw()


def klik(x, y, tlacitko, mod):
    print(tlacitko, mod)
    had.x = x
    had.y = y


window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik,
)

obrazek2 = pyglet.image.load("culebra.png")


def zmen(t):
    had.image = obrazek2  # bez dalsiho radku a fce zmen zpatky zmeni obrazek natrvalo
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)  # za 0.2s zavola fci zmen_zpatky


def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)


pyglet.clock.schedule_once(zmen, 1)  # za 1s zavola fci zmen

pyglet.app.run()
