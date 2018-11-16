import pyglet
import math
window = pyglet.window.Window()


def tik(t):
    had.x = had.x + t * 20 # co je to za hodnotu to t?
    had.y = 300 + 20 * math.sin(had.x / 5)
    # had.rotation = 90.0
    
        
pyglet.clock.schedule_interval(tik, 1/30)


def zpracuj_text(text):
    had.x = 150
    had.rotation = had.rotation + 10
    
obrazek = pyglet.image.load("snake.png")
had = pyglet.sprite.Sprite(obrazek, x=10, y=10)

def vyklesli():
    window.clear()
    had.draw()
    
    
def klik(x, y, tlacicko, mod):
    print(tlacitko, mod)
    had.x = x
    had.y = y
    

window.push_handlers(
    on_text=zpracuj_text, #registrace fce, fci vzdy ve spravny cas zavola - kdyz uzivatel zmackne klavesu
    on_draw=vyklesli,
    on_mouse_press=klik
) 

obrazek2 = pyglet.image.load("culebra.png")


def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)
    
def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)
    
pyglet.clock.schedule_once(zmen, 0.2)
    
pyglet.app.run() # toto je fce, cela smycka udalosti


"""
vypis = print # fce prirazena do promenne
vypis("hello")
print(print)
"""


