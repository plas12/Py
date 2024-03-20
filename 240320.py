'''
import turtle
t = turtle.Turtle()
t.setx(100)
t.sety(100)
t.setx(0)
t.sety(0)

t.clear()

t.goto(100, 0)
t.goto(100, 100)
t.goto(0, 100)
t.goto(0, 0)

t.clear()

t.setheading(180)
t.forward(100)
t.setheading(60)
t.forward(100)
t.setheading(-60)
t.forward(100)

t.clear()




import turtle

t = turtle.Turtle()
t.goto(50, 30)
t.goto(50, -30)
t.goto(-50, 30)
t.goto(-50, -30)
t.goto(0, 0)
turtle.done()


import turtle

t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.right(90)
t.forward(100)
t.right(60)
t.backward(100)
t.right(60)
t.forward(100)

t.clear()

t.setheading(0)

t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)

t.clear()

t.setheading(0)

t.left(60)
t.forward(100)
t.right(60)
t.forward(100)
t.left(120)
t.forward(100)
t.setheading(60)
t.forward(100)

t.left(120)
t.forward(100)
t.right(60)
t.forward(100)
t.left(120)
t.forward(100)
t.right(60)
t.forward(100)

t.setheading(-60)
t.forward(100)
t.setheading(-120)
t.forward(100)
t.setheading(0)
t.forward(100)
t.setheading(-60)
t.forward(100)

t.clear()

t.setheading(0)


import turtle
t = turtle.Turtle()

t.shape("turtle")
t.speed(0)
t.forward(100)
t.pencolor("red")
t.left(120)
t.forward(100)
t.pensize(5)
t.left(120)
t.forward(100)
t.penup()
t.goto(-50, 86.6)
t.pendown()
t.pen(pensize=10, pencolor="blue", speed=10)
t.setheading(330)
t.forward(86.6)
turtle.done()

t.clear()


import turtle
t = turtle.Turtle()


t.speed(1)
t.right(90)
stmp1 = t.stamp()
t.forward(30)
stmp2 = t.stamp()
t.forward(50)
t.undo()
t.clearstamp(stmp1)
t.penup()
t.goto(-20, 0)
t.dot(10)
t.goto(20, 0)
t.dot(10)
t.goto(15, -40)
t.right(75)
t.pendown()
t.circle(-50, 45)

turtle.done()


import turtle
t = turtle.Turtle()

t.shape('turtle')
r = 50
t.circle(r)
t.goto(100, 0)
r = r + 30
t.circle(r)
t.goto(200, 0)
r = r + 30
t.circle(r)
t.home()

t.clear()


import turtle
t = turtle.Turtle()

t.goto(200, 0)
t.goto(200, -50)
t.goto(-200, 50)
t.goto(-200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(50, 200)
t.goto(-50, -200)
t.goto(0, -200)
t.goto(0, 0)


import turtle
t = turtle.Turtle()

t.circle(50)
t.penup()
t.goto(100, 0)
t.pendown()
t.circle(80)
t.penup()
t.goto(200, 0)
t.pendown()
t.circle(110)


import turtle
t = turtle.Turtle()

m = int(input("집의 크기를 입력하세요 :"))

t.goto(m, 0)
t.goto(m, m)
t.goto(0, m)
t.goto(0, 0)
t.goto(0, m)
t.goto(m / 2, m * 2)
t.goto(m, m)
'''

import turtle
t = turtle.Turtle()

m = int(input("반지름 :"))
n = int(input("각도 :"))

t.circle(m, n/4)
stmp1 = t.stamp()
t.circle(m, n/4)
stmp2 = t.stamp()
t.circle(m, n/4)
stmp3 = t.stamp()
t.circle(m, n/4)
stmp4 = t.stamp()
t.clearstamp(stmp1)
t.clearstamp(stmp3)
