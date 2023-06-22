from js import document, window
from pyodide.ffi.wrappers import add_event_listener
from pyodide.ffi import create_proxy
import math, random

canvas = Element('canvas').element
ctx = canvas.getContext('2d')

canvas.style.border = '1px solid black'

colors = ['crimson', 'cyan', 'darkcyan', 'pink', 'violet', 'slategrey']
balls = []

def init():
    balls.clear()

    for i in range(50):
        radius = random.uniform(30, 40)
        x =  random.uniform(2*radius, canvas.width - 2*radius)
        y = random.uniform(2*radius, canvas.height - 2*radius)
        dx = random.uniform(-5, 5)
        dy = random.uniform(-5, 5)
        color = colors[random.randint(0, 5)]
        balls.append(
            Ball({
                'radius': radius,
                'x': x,
                'y': y,
                'dx': dx,
                'dy': dy,
                'color': color,
            })
        )

init()

def animate():
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    for ball in balls:
        ball.draw()

    write_heading()
    write_sub_heading()


window.setInterval(create_proxy(animate), 20)

def resizeCanvas(event):
    canvas.width = window.innerWidth - 18
    canvas.height = window.innerHeight - 18
    init()
resizeCanvas('yes')

add_event_listener(window,"resize", resizeCanvas)
add_event_listener(window,"click", resizeCanvas)

js.console.clear()