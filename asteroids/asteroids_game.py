import pyglet
from pyglet.window import key
import math


objects = list()  # for every object in the game

ROTATION_SPEED = 4  # radians per second

window = pyglet.window.Window(width=900, height=900)


batch = pyglet.graphics.Batch()  # collection for all sprites
batch.draw()  # drawing all the sprites at once

# coordinates = set() nechci mit jako globalni promennou bo lodi bude vice a kazda musi mit vlastni

class Spaceship:
    def __init__(self):
        self.x = x
        self.y = y
        self.x_speed = 200
        self.y_speed = 200
        self.rotation = 0
        self.coordinates = set()  # creating a set for storing coordinates

    def picture(self, file):
        image = pyglet.image.load(file)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)

    def tick(self):  # for moving, rotation, managing the ship
        """
        nemuzu tu mit definovane fce na pressed a released keys bo bych tu metodu nemela jak registrovat dole
        na push_handlers
        Kdyz lod bude ovladana skrze metodu, jak sem natahat vsechny potrebne fce? Nebo ty fce budou naopak nejak
        volat metodu na objektu?
        """


def pressed_keys(self, symbol):
    # coordinates = set() nemuzu mit bo by se to pokazde vynulovalo
    if symbol == key.UP:
        self.coordinates.add("up")
    if symbol == key.LEFT:
        self.add("left")
    if symbol == key.RIGHT:
        self.coordinates.add("right")
    return self.coordinates
    """
    toto se self.coordinates je asi blbost bo fce si nepamatuje, na kterem objektu bezi, ne?
    """


def released_keys(symbol):
    coordinates = set()
    if symbol == key.UP:
        coordinates.discard("up")
    if symbol == key.LEFT:
        coordinates.discard("left")
    if symbol == key.RIGHT:
        coordinates.discard("right")
    return coordinates


ship1 = Spaceship()
ship1.picture(file="NAZEV SOUBORU OBRAZKU")

objects.add(ship1)

window.push_handlers(
    on_draw=self.picture(),
    on_key_press=pressed_keys(),
    on_key_release=released_keys(),
)

pyglet.app.run()
