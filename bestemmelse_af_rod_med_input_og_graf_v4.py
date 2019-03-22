import math
from decimal import Decimal
kvadratrod=int(input('indtast det tal der skal findes kvadratrod af:'))
print('Bestemmelse af kvadratroden af',kvadratrod)
print('se graf for valg af x_0. Når x_0 er valgt lukkes grafen')
#print('f(x)=x**2-',kvadratrod)
#print('f/(x)=2*x')
print('')
import turtle as t

#angiver de maksimale værdier på akserne
# min og max skal være ens
xmin=((math.sqrt(kvadratrod))*3)*(-1)
ymin=(kvadratrod*3)*(-1)
xmax=(math.sqrt(kvadratrod))*3
ymax=kvadratrod*3

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
def laengde(kvadratrod):
    if kvadratrod < 10:
        laengde=round(kvadratrod)
    else:
        laengde=round((kvadratrod)/5)
    return laengde

Laengde_x=laengde(math.sqrt(kvadratrod))
Laengde_y=laengde(kvadratrod)

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
x=0
y=0
t.goto(0,0)
t.pendown()
t.setheading(270)

def funktion(x):
    y=x**2-kvadratrod
    return y

def x_til_v2(kvadratrod):#afgør hvor meget der skal ligges til i nedenstående loop
    if kvadratrod <= 10000:
        x=kvadratrod/200
    elif 10000 < kvadratrod <= 1000000:
        x=kvadratrod/2000
    else:
        x=kvadratrod/8000
    return x

x=0
y=0
x_v=0
while True:
    t.goto(konverter_til_turtle_ks(x_v,funktion(x_v)))
    x_v=x_v+x_til_v2(kvadratrod)
    #print(konverter_til_turtle_ks(x_v,funktion(x_v)))
    if funktion(x_v)>ymax:
        #print(funktion(x_v))
        #print(ymax)
        break

x_resul=int(input('indtast x_0:'))
#t.bye()
print('x 0 =',x_resul)
for n in range(1,1000):
    x_n=x_resul
    x_n_1=n
    x_resul=x_n-((x_n**2)-kvadratrod)/(2*x_n)
    print('x',x_n_1,'=',x_resul)
    if x_n - x_resul <0.00000000000001 and x_n - x_resul > -0.00000000000001:
        print('endeligt resultat:', x_resul)
        print('test af resultat')
        print(x_resul,'*',x_resul,'=',x_resul**2)
        if (x_resul**2-kvadratrod)==0:
            print (kvadratrod)
            print(x_resul**2 - kvadratrod)
            print('den funde kvadratrod er korrekt')
        else:
            print (kvadratrod)
            print(x_resul**2 - kvadratrod)
            print('den funde kvadratrod er tilmærmelsesvis korrekt')
        break
