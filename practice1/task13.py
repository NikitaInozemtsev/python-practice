import math

def f13(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(n+1):
        sum2 += float(math.pow(i, 8) - math.pow(i, 7) / 36)
        sum1 += float(math.sin(i) - 16 * math.pow(i, 8) - 85)
    return "{:.2e}".format(28 * sum1 * m - 82 * sum2)

#print(f13(43, 32))