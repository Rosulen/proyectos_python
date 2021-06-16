import turtle

# Creación y configuración de la ventana principal
wn = turtle.Screen()
wn.title("Diana")
wn.bgcolor("pink")
wn.setup(width=600, height=600)
wn.tracer(0)

# Creación de elementos gráficos (circulos de la diana)
c3 = turtle.Turtle() # c3 - circulo 3
c3.speed(0)
c3.shape("circle")
c3.color("green")
c3.goto(0,-40)
c3.shapesize(24)

c2 = turtle.Turtle() # c2 - circulo 2
c2.speed(0)
c2.shape("circle")
c2.color("yellow")
c2.goto(0,-40)
c2.shapesize(16)

c1 = turtle.Turtle() # c1 - circulo 1
c1.speed(0)
c1.shape("circle")
c1.color("blue")
c1.goto(0,-40)
c1.shapesize(8)

while True:
    wn.update()
