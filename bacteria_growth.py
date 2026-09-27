def bacteries_number(n):
    if n == 0:
        return  5
    else:
        m = (2*bacteries_number(n-1))-n
        return m


def temps():
    nombre = 0
    n = 0
    while nombre < 20000:
        n += 1
        nombre = bacteries_number(n)
    return n

