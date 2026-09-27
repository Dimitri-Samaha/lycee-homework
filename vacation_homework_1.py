def montant_depense(n):
    if n < 200:
        M = n * 0.11
    else:
        M = n * 0.08
    return M


def croissance_village(n):
    p = 2300
    for k in range(1, n+1):
        p = p + 150
    return p

print(croissance_village(0))
