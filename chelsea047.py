def determinan3x3(matriks):
    a = matriks[0][0]
    b = matriks[0][1]
    c = matriks[0][2]

    d = matriks[1][0]
    e = matriks[1][1]
    f = matriks[1][2]

    g = matriks[2][0]
    h = matriks[2][1]
    i = matriks[2][2]

    determinan = (a * (e*i - f*h)
                 - b * (d*i - f*g)
                 + c * (d*h - e*g))

    return determinan
