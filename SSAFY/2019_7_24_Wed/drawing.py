import turtle
t1 = turtle.Turtle()
t1.color('red')
t1.width('5')




def make_sq(tur):
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)


def make_roval(tur):
    x1, y1 = tur.position()
    for i in range(80):
        dx = i
        dy = (0.1*dx)**2
        tur.goto(x1+dx,y1+dy)
    x1, y1 = x1+dx,y1+dy
    tur.goto(x1,y1)
    for j in range(80):     
        dx = j
        dy = (0.1*dx)**2
        tur.goto(x1-dx,y1-dy)

def make_loval(tur):
    x1, y1 = tur.position()
    for i in range(80):
        dx = i
        dy = (0.1*dx)**2
        tur.goto(x1-dx,y1+dy)
    x1, y1 = x1-dx,y1+dy
    tur.goto(x1,y1)
    for j in range(80):     
        dx = j
        dy = (0.1*dx)**2
        tur.goto(x1+dx,y1-dy)

for i in range(int(5)):
    make_sq(t1)
    t1.right(int(90-360/5))


t1.color('yellow')
t1.width('30')
t1.goto(t1.position())
x,y = t1.position()
t1.width('5')
t1.goto(x,y-20)
t1.color('red')
t1.goto(x,y-120)
t1.color('green')

t1.goto(x,y-360)
make_roval(t1)
make_loval(t1)
