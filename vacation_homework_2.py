## exercice 1
n = int(input("L'age du chien est : "))

def conv_age(n):
    if n == 0:
        age_en_homme = 0
    elif n == 1:
        age_en_homme = 20
    elif n == 2:
        age_en_homme = 28
    else:
        age_en_homme = 28 + 4*(n-2)
    return age_en_homme
print("Son age humain est", conv_age(n))

## exercice 2
taille = 1.84
masse = 75
IMC = masse/taille**2
print(IMC)

## exercice3
nb_personne = 4
if nb_personne < 3:
    prix = nb_personne*5
elif nb_personne == 3:
    prix = nb_personne*5*0.9
else:
    prix = nb_personne*5*0.8

## exercice 4
def f(x):
    a = -2*x+4
    return a

u = 0
for i in range(0, 4):
    u = u+f(i)
