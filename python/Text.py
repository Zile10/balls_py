class Text:
    def __init__(self, config):
        self.text = None
        self.x = None
        self.y = None
        self.config

    def write(text, x, y):
        self.text = self.text
        self.x = self.x
        self.y = self.y
        



def write_heading():
    ctx.strokeStyle = '#306998'
    ctx.font = '900 120px sans-serif'
    ctx.shadowColor = '#306998'
    ctx.shadowBlur = 16
    ctx.lineWidth = 4
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.strokeText('Python', canvas.width/2, canvas.height/2 - 0.4 * 120)

def write_sub_heading():
    ctx.fillStyle = '#ffd43b'
    ctx.font = '40px sans-serif'
    ctx.shadowColor = '#ffd43b'
    ctx.shadowBlur = 16
    ctx.lineWidth = 2
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillText('In HTML With PyScript', canvas.width/2, canvas.height/2 + 0.4 * 120)