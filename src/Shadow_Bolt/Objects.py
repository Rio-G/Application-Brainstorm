c = color(255,255,25)
x = 700.0
y = 100.0
speed = 2.0

def draw():
    if mousePressed:
        mount = loadImage("Shadow Mountain.png")
        image(mount, 0, 0)
        bolter = loadImage("Shadow Bolt ninja.gif") 
        image(bolter, -10, 265)
    if keyPressed:
            move()
            display()
def move():
  global x
  x = x - speed
  if x > width:
          x = 0

def display():
  fill(c)
  rect(x, y, 30, 10)
  
