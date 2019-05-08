kvadratrod=int(input('indtast det tal der skal findes kvadratrod af:'))
def x_til(kvadratrod):
    if kvadratrod < 5:
        return 0.05
    if 5<= kvadratrod < 10:
        return 0.075
    if 10< kvadratrod < 20:
        return 0.1

print(x_til(kvadratrod))

def x_til_v2(kvadratrod):
    x=kvadratrod/200
    return x

print(x_til_v2(kvadratrod))
