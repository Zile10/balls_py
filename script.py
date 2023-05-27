from js import console, document, window, requestAnimationFrame
from pyodide.ffi.wrappers import add_event_listener
from pyodide.ffi import create_proxy
import math, random

canvas = Element('canvas').element
ctx = canvas.getContext('2d')

canvas.style.border = '1px solid black'

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


colors = ['crimson', 'cyan', 'darkcyan', 'pink', 'violet', 'slategrey']
balls = []

def init():
    balls.clear()

    for i in range(100):
        radius = 30 + random.random() * 10
        x =  random.random() * (canvas.width - 4 * radius) + radius
        y = random.random() * (canvas.height - 4 * radius) + radius
        dx = random.random() * 5 - 2.5
        dy = random.random() * 5 - 2.5
        color = colors[math.floor(random.random() * 6)]
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

window.setInterval(create_proxy(animate), 25)

def resizeCanvas(event):
    canvas.width = window.innerWidth - 18
    canvas.height = window.innerHeight - 18
    init()
resizeCanvas('yes')

add_event_listener(window,"resize", resizeCanvas)
add_event_listener(window,"click", resizeCanvas)