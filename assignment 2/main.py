import js as p5
from js import document

data = None
isSquare = True
base_color = (134, 255, 203) 
shape_positions = [] 
shape_sizes = [] 
g_value = 128 

def adjust_green(rgb_color, g_value):
    r, _, b = rgb_color
    return (r, g_value, b)

def setup():
    p5.createCanvas(1800, 1000) 
    p5.background(0) 

    for i in range(500):
        x = p5.random(p5.width)
        y = p5.random(p5.height)
        size = p5.random(50, 100)  
        shape_positions.append((x, y))
        shape_sizes.append(size)

def draw():
    global data, isSquare, g_value, shape_positions, shape_sizes
    data = document.getElementById("data").innerText

    if data == 'TOGGLE_SHAPE':
        isSquare = not isSquare
        shape_positions = [(p5.random(p5.width), p5.random(p5.height)) for i in range(500)]
        shape_sizes = [p5.random(50, 150) for i in range(500)]
    else:
        g_value = int(data) 

        
    p5.background(0)

    for (x, y), size in zip(shape_positions, shape_sizes): 
        r, g, b = adjust_green(base_color, g_value)
        p5.fill(r, g, b)

        if isSquare:
            p5.rect(x, y, size, size)
        else:
            p5.ellipse(x, y, size, size)
