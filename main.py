import turtle
screen = turtle.Screen()
screen.screensize(500,500)
screen. bgcolor("Dodger blue")

t = turtle.Turtle()
t.pencolor("white")
t.penup()
t.goto(0,200)
t.pendown()
t.write("All About Me",font=("arial",30,"bold"),align="center")
t.penup()

t.pencolor("white")
t.penup()
t.goto(0,150)
t.pendown()
t.write("Gavin Griffiths",font=("arial",15,"bold"),align="center")
t.penup()
t.goto(0,120)
t.pendown()
t.write("Press enter to continue ",font=("arial",15,"bold"),align="center")
t.penup()

t.goto(0,0)
t.pendown()
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(-200,300)
t.pendown()
screen.addshape("sports.gif")
t.shape("sports.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(200,300)
t.pendown()
screen.addshape("Pirates.gif")
t.shape("Pirates.gif")
t.stamp()



round = input("Press enter to continue")
t.clear()
screen.bgcolor("red")
t.penup()

t.goto(100,0)
t.pendown()
screen.addshape("pizza.gif")
t.shape("pizza.gif")
t.stamp()

t.goto(0,0)
t.pendown()
screen.addshape("spaghetti.gif")
t.shape("spaghetti.gif")
t.stamp()

t.goto(-100,0)
t.pendown()
screen.addshape("taco.gif")
t.shape("taco.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("1) Taco",font=("arial",15,"bold"),align="center")

t.penup()
t.goto(0,170)
t.pendown()
t.pencolor("white")
t.write("2) Spaghetti ",font=("arial",15,"bold"),align="center")

t.penup()
t.goto(0,140)
t.pendown()
t.pencolor("white")
t.write("3) Pizza ",font=("arial",15,"bold"),align="center")

t.penup()
t.goto(0,300)
t.pendown()
t.pencolor("White")
t.write("Favorite Foods",font=("arial",30,"bold"),align="center")

round = input("Press enter to continue")
t.clear()
screen.bgcolor("orange")
t.penup()
t.goto(0,300)
t.pendown()
t.pencolor("White")
t.write("Favorite Hobbies",font=("arial",30,"bold"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
screen.addshape("lifting.gif")
t.shape("lifting.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(100,0)
t.pendown()
screen.addshape("biking.gif")
t.shape("biking.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("1) lifting ",font=("arial",15,"bold"),align="center")


t.penup()
t.goto(0,170)
t.pendown()
t.pencolor("white")
t.write("2) biking ",font=("arial",15,"bold"),align="center")

t.penup()
t.goto(0,140)
t.pendown()
t.pencolor("white")
t.write("3) video games ",font=("arial",15,"bold"),align="center")

t.penup()
t.goto(0,110)
t.pendown()
t.pencolor("white")
t.write("4) drawling ",font=("arial",15,"bold"),align="center")

round = input("Press enter to continue")
t.clear()
screen.bgcolor("tan")
t.penup()
t.goto(0,300)
t.pendown()
t.pencolor("White")
t.write("Favorite Movie",font=("arial",30,"bold"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
screen.addshape("Happy gilmore.gif")
t.shape("Happy gilmore.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(100,0)
t.pendown()
screen.addshape("Happy gilmore 2.gif")
t.shape("Happy gilmore 2.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(0,180)
t.pendown()
t.pencolor("white")
t.write("Happy Gilmore",font=("arial",25,"bold"),align="center")


round = input("Press enter to continue")
t.clear()
screen.bgcolor("purple")
t.penup()
t.goto(0,300)
t.pendown()
t.pencolor("White")
t.write("Favorite Sport",font=("arial",30,"bold"),align="center")

t.penup()
t.goto(0,180)
t.pendown()
t.pencolor("white")
t.write("Baseball",font=("arial",25,"bold"),align="center")


t.penup()
t.goto(-100,0)
t.pendown()
screen.addshape("Baseball.gif")
t.shape("Baseball.gif")
t.stamp()
t.shape("classic")



t.penup()
t.goto(100,0)
t.pendown()
screen.addshape("Baseball 2.gif")
t.shape("Baseball 2.gif")
t.stamp()
t.shape("classic")











turtle.done()
