import turtle as t

#angiver de maksimale værdier på akserne
# min og max skal være ens
xmin=-125
ymin=-125
xmax=125
ymax=125

#angiver hvor mange pixels akserne skal være
# min og max skal være ens
xtmin=-480
ytmin=-380
xtmax=480
ytmax=380
t.setup(width=0.7, height=0.8, startx=None, starty=None)
# sets window to 70% of screen by 80% of screen and centers
t.ht()
t.speed(0)
t.penup()
def konverter_til_turtle_ks(x,y):
    x_in_turtle_kords=x/(xmax-xmin)*(xtmax-xtmin)
    y_in_turtle_kords=y/(ymax-ymin)*(ytmax-ytmin)
    return x_in_turtle_kords, y_in_turtle_kords
x=0
#værdierne af nedenståedne variabler afgør hvor langt der er
#mellem tallene på h.h. x- og y-aksen
Laengde_x=5
Laengde_y=5

t.pendown()
while True:
    t.goto(konverter_til_turtle_ks(x,0))
    t.left(90)
    t.forward(5)
    t.write(x)
    t.back(10)
    t.forward(5)
    t.right(90)
    x=x+Laengde_x
    if x > xmax:
        break
x=0
y=0
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(90)
while True:
    t.goto(konverter_til_turtle_ks(0,y))
    t.left(90)
    t.forward(5)
    t.back(10)
    t.write(y)
    t.forward(5)
    t.right(90)
    y=y+Laengde_y
    if y > ymax:
        break
x=0
t.goto(0,0)
t.pendown()
t.setheading(180)
while True:
    t.goto(konverter_til_turtle_ks(-x,0))
    t.left(90)
    t.forward(5)
    t.back(10)
    t.write(-x)
    t.forward(5)
    t.right(90)
    x=x+Laengde_x
    if x > xmax:
        break
x=0
y=0
t.goto(0,0)
t.pendown()
t.setheading(270)
while True:
    t.goto(konverter_til_turtle_ks(0,-y))
    t.left(90)
    t.forward(5)
    t.write(-y)
    t.back(10)
    t.forward(5)
    t.right(90)
    y=y+Laengde_y
    if y > ymax:
        break
    
