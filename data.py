import turtle
import colorsys

# Setup screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Color setup
hue = 0
n = 36  # Number of layers
colors = [colorsys.hsv_to_rgb(hue + i/n, 1, 1) for i in range(n)]

# Convert RGB from 0-1 to 0-255
colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]
screen.colormode(255)

# Draw mandala pattern
def draw_mandala():
    for j in range(12):  # Main petals
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(j * 30)
        
        for i in range(n):
            t.color(colors[i])
            t.circle(100 - i*2, 60)
            t.left(60)
            t.circle(100 - i*2, 60)
            t.left(60)

# Draw decorative outer ring
def draw_outer_ring():
    t.penup()
    t.goto(0, -250)
    t.setheading(0)
    t.pendown()
    
    for i in range(72):
        t.color(colors[i % n])
        t.circle(250, 5)
        t.left(95)
        t.forward(20)
        t.backward(20)
        t.right(95)

draw_mandala()
draw_outer_ring()

t.hideturtle()
turtle.done()
