import math
def f14(n):
    if n == 0:
        return 3
    elif n == 1:
        return 5
    else:
        return math.cos(f14(n - 2)) - math.sin(f14(n - 2))

#print(f14(8))