def f22(x):
    temp = bin(x)[2:].zfill(32)
    a = temp[28:]
    a = int(a, 2)
    a <<= 10
    b = temp[18:28]
    b = int(b, 2)
    c = temp[11:18]
    c = int(c, 2)
    c <<= 19
    d = temp[6:11]
    d = int(d, 2)
    d <<= 27
    e = temp[5]
    e = int(e, 2)
    e <<= 18
    f = temp[2:5]
    f = int(f, 2)
    f <<= 15
    g = temp[1]
    g = int(g, 2)
    g <<= 14
    h = temp[0]
    h = int(h, 2)
    h <<= 26
    res = a | b | c | d | e | f | g | h
    return  res


#print(f22(0xb2172f7f))
