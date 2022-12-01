import math

def normalizar(a):
    return math.sqrt( a[2]**2+ a[1]**2 +  a[0]**2)

def pCruz(a, b):
    l1 = len(a)
    l2 = len(b)
    if l1 == l2 and l1 == 3:
        resultado = [a[1]*b[2] - a[2]*b[1],
                     a[2]*b[0] - a[0]*b[2],
                     a[0]*b[1] - a[1]*b[0]]
        return resultado

def determinante2(*a):
    resultado =  a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return resultado

#
def determinante3(a):
    resultado = a[0][0] * determinante2(a[1][1:3], a[2][1:3]) - a[0][1] * determinante2([a[1][0], a[1][2]], [a[2][0], a[2][2]]) + a[0][2] * determinante2(a[1][0:2], a[2][0:2])
    return resultado


def determinante4(a):
    temp = []
    for i in range(4):
        b= M4a3(a, 0, i)
        t = a[0][i] * determinante3(b)
        temp.append(t)

    resultado = temp[0] - temp[1] + temp[2] - temp[3]

    return resultado


def pPunto(a, b):
    producto = 0
    for a,b in zip(a,b):
        producto = producto + a * b

    return producto


def dividir(vector: tuple, normal: float):
    resultado = tuple(map(lambda item: item / normal, vector))

    return resultado

def restaVect(a, b):

    resultado = []

    for i in range(min(len(a), len(b))):
        resultado.append(a[i] - b[i])

    return resultado

def mvMatriz4 (a, b):
    resultado = []

    for i in range(4):
        c = 0
        for j in range(4):
            c += a[i][j] * b[j]
        resultado.append(c)

    return resultado

def dMatriz(a, b):
    resultado = []
    for i in range(len(a)):
        c = len(a[i])
        temp = []
        for j in range(c):
            temp.append(a[i][j] / b)
        resultado.append(temp)

    return resultado

def colAren(a):
    resultado = [[], [], [], []]

    for i in range(4):
        resultado[i] = [a[0][i], a[1][i], a[2][i], a[3][i]]

    return resultado


def mMatriz4(a, b):
    c = colAren(b)
    resultado = []

    for n in range(4):
        temp = []

        for i in range(4):
            d = 0
            for j in range(4):
                d += a[n][j] * c[i][j]
            temp.append(d)
            d = 0
        resultado.append(temp)

    return resultado

def radianes(a):
    radian = a * 3.1416
    radian = radian / 180

    return radian

def renAcol(a):
    resultado = [[], [], [], []]

    for i in range(4):
        vector = a[i]
        resultado[0].append(vector[0])
        resultado[1].append(vector[1])
        resultado[2].append(vector[2])
        resultado[3].append(vector[3])

    return resultado

def invMatriz(a):
    b = renAcol(a)

    c = []
    d = True

    for i in range(4):
        temp = []
        for j in range(4):
            d = M4a3(b, i, j)
            determinante_ = determinante3(d)
            if d:
                temp.append(determinante_)
            else:
                temp.append(-(determinante_))
            sign = not d
        d = not d
        c.append(temp)

    det = determinante4(a)
    return dMatriz(c, det)




def M4a3(a, y, x):
    resultado = []
    for i in range(4):
        temp = []
        for j in range(4):
            if y != i and x != j:
                temp.append(a[i][j])
        if len(temp) == 3:
            resultado.append(temp)
    return resultado
