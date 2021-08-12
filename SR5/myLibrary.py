

def crossProduct(vector1, vector2):
    if len(vector1) == 3 and len(vector2) == 3:
        i = vector1[1]*vector2[2] - vector2[1]*vector1[2]
        j = vector1[0]*vector2[2] - vector2[0]*vector1[2]
        k = vector1[0]*vector2[1] - vector2[0]*vector1[1]
        return [i, -j, k]
    if len(vector1) == 2 and len(vector2) == 2:

        k = vector1[0]*vector2[1] - vector2[0]*vector1[1]
        return [k]
    else:

        return 'invalid arguments'


def subtract(vector1, vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x]-vector2[x])
        return newVector


def getVectorMagnitude(vector):
    totalSquared = 0
    for x in vector:
        totalSquared += pow(x, 2)
    return pow(totalSquared, .5)


def normalize(vector1):
    newVector = []
    magnitude = getVectorMagnitude(vector1)
    for x in vector1:
        if magnitude != 0:
            newVector.append(x/magnitude)
        else:
            newVector.append(x)
    return newVector


def dotProduct(vector1, vector2):
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        total = 0
        for x in range(len(vector1)):
            total += vector1[x]*vector2[x]
        return total
