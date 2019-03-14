kvadratrod=int(input('indtast det tal der skal findes kvadratrod af:'))
import math
def x_til(kvadratrod):#afgør hvor meget der skal ligges til i nedenstående loop
    if kvadratrod < 5:
        return 0.05
    if 5<= kvadratrod < 10:
        return 0.075
    if 10< kvadratrod < 20:
        return 0.1

print(x_til(kvadratrod))


def x_til_v2(kvadratrod):#afgør hvor meget der skal ligges til i nedenstående loop
    x=kvadratrod/200
    return x

print(x_til_v2(kvadratrod))
print (math.sqrt(1000))
