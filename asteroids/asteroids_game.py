import pyglet
from pyglet.window import key
import math


objects = list()  # for every object in the game

ROTATION_SPEED = 4  # radians per second

window = pyglet.window.Window(width=900, height=900)


batch = pyglet.graphics.Batch()  # collection for all sprites
batch.draw()  # drawing all the sprites at once


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



def pressed_keys(self, symbol):
    if symbol == key.UP:
        self.coordinates.add("up")
    if symbol == key.LEFT:
        coordinates.add("left")
    if symbol == key.RIGHT:
        coordinates.add("right")
    return coordinates


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
