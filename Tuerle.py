import turtle
turtle.shape('square')
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.goto(0,100)
turtle.stamp()
turtle.goto(0,0)
turtle.stamp()
turtle.goto(-100,0)
turtle.stamp()
turtle.goto(-100,100)


triangle= turtle.clone()
triangle.shape('triangle')
triangle.penup()
triangle.goto(50,50)
triangle.pendown()
triangle.goto(150,50)
triangle.stamp()
triangle.goto(100,100)
triangle.stamp()
triangle.goto(50,50)

square=turtle.clone()
square.shape('turtle')
square.penup()
square.goto(25,25)
square.stamp()
square.goto(100,150)

