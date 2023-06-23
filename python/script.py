from js import document, window, console
from pyodide.ffi.wrappers import add_event_listener
from pyodide.ffi import create_proxy
import math, random

canvas = Element('canvas').element
ctx = canvas.getContext('2d')

canvas.style.border = '1px solid black'

mouse = {
    'x': 0,
    'y': 0,
    'canvasX': 9,
    'canvasY': 9,
    'isDown': False,
    'dragging': None
}

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
                'id': i + 1
            })
        )

init()

def animate():
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    for ball in balls:
        ball.draw()

    ctx.fillStyle = 'rgba(0,0,0, 0.3)'
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    write_heading()
    write_sub_heading()


window.setInterval(create_proxy(animate), 20)

def resizeCanvas(event):
    canvas.width = window.innerWidth - 18
    canvas.height = window.innerHeight - 18
    init()
resizeCanvas('yes')

def mouseMove(e):
    mouse['x'] = e.clientX
    mouse['y'] = e.clientY
    mouse['canvasX'] = mouse['x'] + 9
    mouse['canvasY'] = mouse['y'] + 9

# def dragger(e):
#     for ball in balls:
#         if ball.x - ball.radius < mouse['canvasX'] and ball.x + ball.radius > mouse['canvasX'] and ball.y - ball.radius < mouse['canvasY'] and ball.y + ball.radius > mouse['canvasY'] :
#             ball.drag()
def mouseDown(e):
    mouse['isDown'] = True
    for ball in balls:
        isUnderMouse = ball.x - ball.radius < mouse['canvasX'] and ball.x + ball.radius > mouse['canvasX'] and ball.y - ball.radius < mouse['canvasY'] and ball.y + ball.radius > mouse['canvasY']
        if isUnderMouse and mouse['isDown']:
            mouse['dragging'] = ball.id

def mouseUp(e):
    mouse['isDown'] = False
    mouse['dragging'] = None

add_event_listener(window,"resize", resizeCanvas)
add_event_listener(canvas,"mousemove", mouseMove)
add_event_listener(canvas,"mousedown", mouseDown)
add_event_listener(canvas,"mouseup", mouseUp)


js.console.clear()