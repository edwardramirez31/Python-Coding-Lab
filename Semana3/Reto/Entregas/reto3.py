#Al igual que el reto 2, solo es ejecutar python reto3.py para que muestre todas las salidas a la vez.
import numpy as np

def extractOdds():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr = arr[arr % 2 == 1]
    print(arr)

extractOdds()

def convertToNegative():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr % 2 == 1] = -1
    print(arr)

convertToNegative()

def convertMatrixVert():
    a = np.arange(10).reshape(2,-1)
    b = np.repeat(1, 10).reshape(2,-1)

    c = np.vstack([a, b])

    print(c)

convertMatrixVert()

def concatMatrix():
    a = np.arange(10).reshape(2,-1)
    b = np.repeat(1, 10).reshape(2,-1)

    c = np.concatenate([a, b], axis=1)

    print(c)

concatMatrix()

def generateSecuenceNumpy():
    arr = np.arange(10)
    print(arr)

generateSecuenceNumpy()

def getCommomValues():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    c = a[np.in1d(a, b)]
    print(c)

getCommomValues()

def getIndexEqualValues():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])

    c = np.where(a == b)

    print(c)

getIndexEqualValues()

def extracRangeValues():

    a = np.array([2, 6, 1, 9, 10, 3, 27])

    b = np.where(np.logical_and(a >= 5, a <= 10))

    print(b)

extracRangeValues()