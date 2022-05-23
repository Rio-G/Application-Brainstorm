c = color(255,255,25)
x = 700.0
y = 100.0
speed = 5.0
b = False
def setup():
    size(700,525);
    moon = loadImage("Start screen.gif")
    image(moon, 0, 0)
    title = loadImage("shadow title.png") 
    image(title, 35, 300)
    click = loadImage("Click.png") 
    image(click, 70, 450)

def draw(): 
    if mousePressed:
        mount = loadImage("Shadow Mountain.png")
        image(mount, 0, 0)
        bolter = loadImage("Shadow Bolt ninja.gif") 
        image(bolter, -10, 265)
        display()
        move()

def mousePressed():
    b = True
    if b == True:
        move()

def move():
  global x
  x = x - speed
  if x < 0:
          x = width

def display():
  fill(c)
  rect(x, y, 30, 10)     
