import turtle
t=turtle
t.shape('turtle')
"""def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()
def rectangle(x):
    t.forward(x)
    t.left(90)
    t.forward(x+250)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x+250)
    t.left(90)
rectangle(200)"""
for i in range(3):
    print(i)
    for i in range(4):
    t.forward(100)
    t.left(90)
    sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
        t.left(5)
addSquares(60)



   





    