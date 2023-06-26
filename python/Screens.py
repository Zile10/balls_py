class Screen:
    def __init__(self, background, middleground, foreground):
        self.background = background
        self.middleground = middleground    
        self.foreground = foreground
    
    def draw(self):
        ctx.clearRect(0, 0, canvas.width, canvas.height) # Clear Canvas
        # Draw Background
        for elem in self.background:
            elem.draw()
        # Draw Middle
        for elem in self.middleground:
            elem.draw()
        # Draw Foreground
        for elem in self.foreground:
            elem.draw()
