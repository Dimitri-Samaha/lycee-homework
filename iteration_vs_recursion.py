t = int(input("t = "))

## Method 1
def iteration(t):
    n = 5
    for i in range(1, t+1):
        n = (2 * n) - i
    return n


print(iteration(t))

## Method 2
def recursion(t):
    if t == 0:
        return 5
    else:
        return (2 * recursion(t-1))-t

print(recursion(t))
