from js import console, document, window
from pyodide.ffi.wrappers import add_event_listener
import math, random

canvas = Element('canvas').element
ctx = canvas.getContext('2d')

canvas.style.border = '1px solid black'
def resizeCanvas(event):
    canvas.width = window.innerWidth - 18
    canvas.height = window.innerHeight - 18
resizeCanvas('yes')

add_event_listener(window,"resize", resizeCanvas)

class Ball:
    def __init__(self, config):
        self.x = config['x']
        self.y = config['y']
        self.dx = config['dx']
        self.dy = config['dy']
        self.radius = config['radius']
        self.color = config['color']
        self.gravity = 1
        self.friction = 0.97
    
    def draw(self):
        ctx.beginPath()
        ctx.fillStyle = self.color
        ctx.strokeStyle = 'black'
        ctx.arc(self.x, self.y, self.radius, 0, 2* math.pi)
        ctx.fill()
        ctx.stroke()
        self.update()

    def update(self):
        if self.x + self.radius + self.dx > canvas.width or self.x - self.radius + self.dx < 0:
            self.dx = - self.dx * self.friction
        if self.y + self.radius + self.dy > canvas.height or self.y - self.radius + self.dy < 0:
            self.dy = - self.dy * self.friction**2
            self.dx = self.dx * self.friction**0.5
        else:
            self.dy += self.gravity
        self.x += self.dx
        self.y += self.dy


def init(event):
    balls = []

    for i in range(100):
        radius = 20 + random.random() * 10
        x = canvas.width * ((random.random() + radius) - 2*radius)
        y = canvas.height * ((random.random() + radius) - 2*radius)
        dx = random.random() * 5 - 2.5
        dy = random.random() * 5 - 2.5
        color = 'crimson'

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
    
    for ball in balls:
        ball.draw()

add_event_listener(document, 'DOMContentLoaded', init)