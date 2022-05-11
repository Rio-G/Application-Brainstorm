def setup():
    size(700,525);
    mount = loadImage("Shadow Mountain.png")
    image(mount, 0, 0)
    bolter = loadImage("Shadow Bolt ninja.gif") 
    image(bolter, -10, 265)
    title = loadImage("shadow title .png") 
    image(title, 20, 50)

def draw(): 
    if mousePressed:
        fill(0)
    else:
        fill(255)
    rect(400, 240, 200, 90)
