import pyglet
from pyglet.window import key
from pyglet import gl
from math import sin, cos, atan2, sqrt, degrees


objects = list()  # for every object in the game

ROTATION_SPEED = 4  # radians per second
ACCELERATION = 15
WIDTH = 1200
HEIGHT = 900

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


batch = pyglet.graphics.Batch()  # collection for all sprites

coordinates = set()


class SpaceObject:
    def __init__(self, x, y, x_speed, y_speed, rotation):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rotation


class Spaceship(SpaceObject):
    def __init__(self, file):
        image = pyglet.image.load(file)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y, batch=batch)

    def tick(self, dt):  # for moving, rotation, managing the ship
        # rotation
        if "right" in coordinates:
            self.rotation = self.rotation + dt * ROTATION_SPEED  # in radians
        if "left" in coordinates:
            self.rotation = self.rotation - dt * ROTATION_SPEED
        self.sprite.rotation = 90 - degrees(self.rotation)  # radians into degrees
        # moving with acceleration
        self.x_speed += dt * ACCELERATION
        self.y_speed += dt * ACCELERATION
        # print(self.x_speed, self.y_speed)
        # basic movement
        if "forward" in coordinates:
            self.x = self.x + dt * self.x_speed * cos(self.rotation)
            self.y = self.y + dt * self.y_speed * sin(self.rotation)
        """returning the ship into the field
        if self.x == WIDTH:
            self.x = 0
        if self.x == 0:
            self.x = WIDTH
        if self.y == HEIGHT:
            self.y = 0
        if self.y == 0:
            self.y = HEIGHT"""
        #print(self.x, self.y)
        self.sprite.x = self.x
        self.sprite.y = self.y



def pressed_keys(symbol, modifiers):
    if symbol == key.UP:
        coordinates.add("forward")
    if symbol == key.LEFT:
        coordinates.add("left")
    if symbol == key.RIGHT:
        coordinates.add("right")
    return coordinates  # voluntary


def released_keys(symbol, modifiers):
    if symbol == key.UP:
        coordinates.discard("forward")
    if symbol == key.LEFT:
        coordinates.discard("left")
    if symbol == key.RIGHT:
        coordinates.discard("right")
    return coordinates  # voluntary


ship1 = Spaceship(file="ship.png")
objects.append(ship1)
ship1.sprite.scale = 0.3


def draw():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # remember the current state
            gl.glPushMatrix()
            # move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # draw
            batch.draw()

            # restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()


window.push_handlers(
    on_draw=draw,
    on_key_press=pressed_keys,
    on_key_release=released_keys,
)

pyglet.clock.schedule(SpaceObject.tick)
pyglet.app.run()
