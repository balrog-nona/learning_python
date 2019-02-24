import pyglet
from pyglet.window import key
import math


objects = list()  # for every object in the game

ROTATION_SPEED = 4  # radians per second
ACCELERATION = 1.5
WIDTH = 900
HEIGHT = 900

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


batch = pyglet.graphics.Batch()  # collection for all sprites
batch.draw()  # drawing all the sprites at once

coordinates = set()


class Spaceship:
    def __init__(self, file):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_speed = 200
        self.y_speed = 200
        self.rotation = 0
        image = pyglet.image.load(file)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y, batch=batch)
        self.sprite.rotation = self.rotation

    """def tick(self):  # for moving, rotation, managing the ship
        # basic movement
        if "right" in coordinates:
        if "left" in coordinates:
        if "forward" in coordinates:
        self.x = self.x + dt * self.x_speed
        self.y = self.y + dt * self.y_speed
        self.rotation = self.rotation + dt * ROTATION_SPEED
        # moving with acceleration
        self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
        self.y_speed += dt * ACCELERATION * math.sin(self.rotation)
        
        toto si musim dat pak do obnov stav a zaevidovat do neceho, co se vola periodicky
        vytvorit pyglet.clock.schedule(metoda) - a tam se navaze metoda
        neumim vytvorit logiku posunu a otaceni lodi - v pongu se nic netocilo kolem sve osy...
        
    """


def pressed_keys(symbol):
    if symbol == key.UP:
        coordinates.add("forward")
    if symbol == key.LEFT:
        coordinates.add("left")
    if symbol == key.RIGHT:
        coordinates.add("right")
    return coordinates


def released_keys(symbol):
    if symbol == key.UP:
        coordinates.discard("forward")
    if symbol == key.LEFT:
        coordinates.discard("left")
    if symbol == key.RIGHT:
        coordinates.discard("right")
    return coordinates


ship1 = Spaceship(file="ship.png")
objects.append(ship1)
ship1.sprite.scale = 0.3

# ship1.x = 700
# ship1.sprite.x = ship1.x

window.push_handlers(
    on_draw=batch.draw,
    on_key_press=pressed_keys,
    on_key_release=released_keys,
)

# pyglet.clock.schedule(ship1.tick)
pyglet.app.run()
