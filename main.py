from turtle import position
from ursina import * 
import random

random_generator = random.Random()


def update():
    for entity in cubes:
        entity.rotation_y += time.dt * 100
    if held_keys['q']:
        camera.position += (0, time.dt, 0)
    if held_keys['a']:
        camera.position -= (0, time.dt, 0)

def input(key):
    if key == 'space':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        cube.color = color.rgb(red, green, blue)
    if key == 'c':
        x = random_generator.random() * 10 - 5
        y = random_generator.random() * 10 - 5
        z = random_generator.random() * 10 - 5
        s = random_generator.random() * 1
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        newcube = Entity(model='cube', color=color.rgb(red, green, blue), position=(x, y, z), scale=(s,s,s))
        cubes.append(newcube)

        childcube = Entity(parent=newcube, model='cube', color=color.rgb(red, green, blue), position=(1,0,0), scale=(s/2,s/2,s/2))
        cubes.append(childcube)


app = Ursina()

window.title = 'Mi juego'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

cubes = []
cube = Entity(model='cube', color=color.white, scale= (2,2,2), texture="crate")
cubes.append(cube)

app.run() 