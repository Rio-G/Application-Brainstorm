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
