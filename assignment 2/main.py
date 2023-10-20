import js as p5
from js import document

data = None

def setup():
  p5.createCanvas(400, 400)
  print('hello p5!')

def draw():
  p5.background(255)

  global data
  data = document.getElementById("data").innerText
  
  circle_size = int(data)
  p5.noStroke()
  p5.fill(150)
  #p5.ellipse(150, 150, circle_size, circle_size)
  p5.push()
  angle = int(data)
  p5.translate(p5.width/2,p5.height/2)
  #degree to radians:
  p5.rotate(p5.radians(angle))
  p5.rectMode(p5.CENTER)
  p5.rect(0,0,100,100)
  p5.pop()
  



def print_test(x):
  print(x)