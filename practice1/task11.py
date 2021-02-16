import math

def f11(x, y, z):
    return "{:.2e}".format(math.sqrt(math.e ** y + 24 * y ** 6 + 78) - (19 * y ** 3 - z ** 2)/(math.cos(x) + math.tan(z)) + 30 * x ** 3 + math.e ** z)

#print(f11(46, -94, -71))