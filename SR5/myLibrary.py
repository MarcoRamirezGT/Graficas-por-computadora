
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


def deg2rad(data):

    pi = 22/7
    degree = data
    radian = degree*(pi/180)
    return radian


def multiplyMatrices(matrix1, matrix2):
    newMatrix = [[0 for i in range(len(matrix2[0]))]
                 for j in range(len(matrix1))]

    for col in range(len(newMatrix[0])):
        vec = [0 for j in range(len(matrix2))]
        for row in range(len(matrix2)):
            vec[row] = matrix2[row][col]
        for row in range(len(newMatrix)):
            d = dotProduct(matrix1[row], vec)
            newMatrix[row][col] = d
    return newMatrix


def add(vector1, vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x]+vector2[x])
        return newVector


def invertedAugmentMatrix(matrix):
    invertedAugmentMatrix = [[0.00 for i in range(
        len(matrix[0]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            invertedAugmentMatrix[row][col] = matrix[row][col]

    index = 0
    matrixWidth = len(invertedAugmentMatrix[0])
    for row in invertedAugmentMatrix:
        for i in range(matrixWidth):
            if i == index:
                row.append(1)
            else:
                row.append(0)
        index += 1
    return invertedAugmentMatrix


def scaleElements(matrix, scalar):
    if isinstance(matrix[0], list):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = matrix[row][col]*scalar
    else:
        newVector = [0 for j in range(len(matrix))]
        for x in range(len(matrix)):
            if matrix[x] != 0:
                newVector[x] = matrix[x]*scalar

        return newVector


def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        return 'Matrix is non invertible'
    else:
        invertedMatrix = invertedAugmentMatrix(matrix)
        matrixWidth = len(matrix[0])
        row = 0
        curRow = 0
        col = 0
        lastPivRow = 0
        lastPivCol = 0

        while col < matrixWidth and curRow < len(invertedMatrix):
            if invertedMatrix[curRow][col] != 0:
                lastPivRow = curRow
                lastPivCol = col
                invertedMatrix[curRow] = scaleElements(
                    invertedMatrix[curRow], 1/(invertedMatrix[curRow][col]))
                row = curRow+1
                while row < len(invertedMatrix):
                    scalar = invertedMatrix[row][col] / \
                        invertedMatrix[curRow][col]
                    invertedMatrix[row] = add(scaleElements(
                        invertedMatrix[curRow], -scalar), invertedMatrix[row])
                    row += 1
                curRow += 1
            else:
                row = curRow+1
                while row < len(invertedMatrix):
                    if invertedMatrix[row][col] != 0:
                        temp = invertedMatrix[curRow]
                        invertedMatrix[curRow] = invertedMatrix[row]
                        invertedMatrix[row] = temp
                        col -= 1
                        break
                    row += 1
            col += 1

        col = lastPivCol
        curRow = lastPivRow

        while col != 0:
            if invertedMatrix[curRow][col] != 0:
                row = curRow-1
                while row != -1:
                    scalar = invertedMatrix[row][col] / \
                        invertedMatrix[curRow][col]
                    invertedMatrix[row] = add(scaleElements(
                        invertedMatrix[curRow], -scalar), invertedMatrix[row])
                    row -= 1
                curRow -= 1
            col -= 1

# #     for row in range(len(invertedMatrix)):
# #         invertedMatrix[row] = invertedMatrix[row][matrixWidth:]
# #     return invertedMatrix


# # camMatrix = np.matrix([[0.89442719, 0.18257419, -0.40824829, -5],
# #                        [-0, 0.91287093, 0.40824829, 5],
# #                        [0.4472136, -0.36514837, 0.81649658, 0],
# #                        [0, 0, 0, 1]])

# # print(camMatrix)

# # print(invertedAugmentMatrix(camMatrix))
# #a = [0.1115538, 0.477012, -8.054662, 1]
# x, y = 4, 1

# a = [[0 for x in range(x)] for y in range(y)]
# a[0][0] = 0.0854448
# a[0][1] = 0.103577
# a[0][2] = 0.606979
# a[0][3] = 1

# w, h = 4, 4
# b = [[0 for x in range(w)] for y in range(h)]
# b[0][0] = 3
# b[0][1] = 0
# b[0][2] = 0
# b[0][3] = 0
# b[1][0] = 0
# b[1][1] = 3
# b[1][2] = 0
# b[1][3] = 0
# b[2][0] = 0
# b[2][1] = 0
# b[2][2] = 3
# b[2][3] = -10
# b[3][0] = 0
# b[3][1] = 0
# b[3][2] = 0
# b[3][3] = 1

# #print(a, b)
# #print(multiplyMatrices(a, b))
# # resultado  [[ 0.2563344 -0.310731  -8.179063   1.       ]]
# print(a)
