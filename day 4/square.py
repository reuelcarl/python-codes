# import turtle


# turtle.color("blue", "green")
# def rectangle():
#     turtle.forward(150)
#     turtle.left(75)
#     turtle.forward(170)
#     turtle.left(75)
#     turtle.forward(170)
#     turtle.left(75)
#     turtle.forward(170)
#     turtle.left(75)
#     turtle.forward(150)
#     turtle.left(170)

# turtle.begin_fill()
# rectangle()
# turtle.end_fill()

# turtle.done()


import turtle

screen = turtle.getscreen()
pen = turtle.Turtle()
pen.forward(100)
pen.backward(200)
pen.reset() 
pen.right(90) 
pen.left(90)
pen.begin_fill() 
pen.fillcolor("green")
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.end_fill()
for i in range(2):
        pen.begin_fill()
        pen.fillcolor("green")
        pen.forward(50)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.end_fill(90)
        def rectangle(colour):
            for i in range(2):
                    pen.begin_fill()
        pen.fillcolor(color) # change from "green " to "red"
        pen.forward(50)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.end_fill(90)
pen.reset()
rectangle("red")
pen.pensize(4)
pen.penup()
pen.goto(0,-200) 
pen.pendown() 
pen.left(90) 
pen.forward(400)
pen.right(90)
rectangle("green")
pen.forward(50)
rectangle("white")
pen.forward(50)
rectangle("green")
pen.forward(50)
pen.hideturtle()