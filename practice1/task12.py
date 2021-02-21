import math

def f12(x):
    res = 0
    if(x < 12):
        res = math.sin(math.cos(x) + abs(x) - 70) - abs(x) - 66
    elif(x >= 12 and x < 78):
        res = 27 * x +69 * x ** 6 - 93
    else:
        res = math.tan(x + x ** 3) - math.tan(x ** 4 + 25 * x ** 2)
    return res

#print(f12(127))