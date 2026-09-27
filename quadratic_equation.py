from math import *

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))


def scnd_deg(a, b, c):
    d = b**2 - 4 * a * c
    print("le discriminant est",d)
    if d == 0:
        x = (-b) / 2 * a
        return print("La racine de cette équation de second degrée est", x)
    elif d > 0:
        x_1 = (sqrt(d)-b) / 2 * a
        x_2 = - (sqrt(d)-b) / 2 * a
        return print("Les racines de cette équation de second degrée sont", round(x_1, 2), "et",round(x_2, 2))
    else:
        return print("Cett équation de second degrée n'admet pas de racine.")



scnd_deg(a, b, c)
