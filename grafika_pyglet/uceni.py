import pyglet
import math
window = pyglet.window.Window()


def tik(t):
    had.x = had.x + t * 70 # co je to za hodnotu to t?
    had.y = 100 + 20 * math.sin(had.x / 5)
    had.rotation = 180.0
    
        
pyglet.clock.schedule_interval(tik, 1/30)


def zpracuj_text(text):
    had.x = 150
    
obrazek = pyglet.image.load("snake.png")
had = pyglet.sprite.Sprite(obrazek)

def vyklesli():
    window.clear()
    had.draw()

window.push_handlers(
    on_text=zpracuj_text, #registrace fce
    on_draw=vyklesli
) 
    
pyglet.app.run() # toto je fce


"""
vypis = print # fce prirazena do promenne
vypis("hello")
print(print)
"""


