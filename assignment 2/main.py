import js as p5
from js import document

data = None
isSquare = True
base_color = (134, 255, 203) 
shape_positions = [] 
shape_sizes = [] 
g_value = 128 

def adjust_green(rgb_color, g_value):
    r = rgb_color[0] 
    b = rgb_color[2] 
    return (r, g_value, b)

def setup():
    p5.createCanvas(1800, 1000) 
    for i in range(300):
        x = p5.random(p5.width)
        y = p5.random(p5.height)
        size = p5.random(50, 100)  
        shape_positions.append((x, y))
        shape_sizes.append(size)

def draw():
    p5.background(40)
    global data, isSquare, g_value, shape_positions, shape_sizes
    data = document.getElementById("data").innerText

    if data == 'TOGGLE_SHAPE':
        if isSquare:
            isSquare = True
        else:
            isSquare = False
        isSquare = not isSquare
        shape_positions = [] 
        shape_sizes = []
        for i in range(300):
            shape_positions.append((p5.random(p5.width), p5.random(p5.height)))
        for i in range(300):
            shape_sizes.append(p5.random(50, 150))

    else:
        g_value = int(data) 

    for i in range(len(shape_positions)):
        x, y = shape_positions[i]
        size = shape_sizes[i]
        r, g, b = adjust_green(base_color, g_value)
        p5.fill(r, g, b)

        if isSquare:
            p5.rect(x, y, size, size)
        else:
            p5.ellipse(x, y, size, size)