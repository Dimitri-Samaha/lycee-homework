## Le problem de Fibonacci:

## Donnees:
## On commence par 2 lapins; 1male et 1 femelle au premier mois
## Les lapins doivent etre age de minimum 1 mois pour se reproduire
## La reproduction de lapins donne toujours; 1 male et 1 femelle
## Les lapins peuvent se reproduire une fois par mois
## Les lapins ne meurent jamais

## La question:
## Combien il y aura de lapin dans 1 an?



t = int(input("months = "))


print("Recursion")


def recursion(t):
    if t == 0 or t == 1:
        return 1
    else:
        return recursion(t-1)+recursion(t-2)


print(recursion(t))
 

print("Iteration list")

def iteration(t):
    calculated = [1, 1]
    for i in range(2, t+1):
        calculated.append(calculated[i-1] + calculated[i-2]) 
    return calculated[t]

print(iteration(t))

print("Iteration variables")

def iteration_var(t):
    current = 1
    previous = 1
    if t == 0 or t == 1:
        return current
    for i in range(2, t+1):
        next_term = current + previous
        previous = current
        current = next_term
    return current

print(iteration_var(t))
