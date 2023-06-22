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
        ctx.shadowBlur = 0
        ctx.lineWidth = 1
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
