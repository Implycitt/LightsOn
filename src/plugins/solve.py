import numpy, sympy

from plugins import Window

class Solve:

    size = 0
    p = []
    b = []
    A = []

    def setStartMatrix(self, p):
        self.p = numpy.array(p)

    def setSize(self, s):
        self.size = s

    def setEndMatrix(self):
        self.b = numpy.array([1 for i in range(self.size**2)])

    def constructTransform(self):

        x = 0
        y = 0
        start = 0
        I = []
        O = []
        B = []
        ret = []

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.insert(j, 0)
            O.insert(i, row)

        for i in range(self.size):
            retRow = []
            row = []
            Brow = []
            for j in range(self.size):
                retRow.insert(j, O)
                Brow.insert(j, 0)
                if (start == j):
                    row.insert(j, 1)
                else:
                    row.insert(j, 0)
            start += 1
            ret.insert(i, retRow)
            I.append(row)
            B.append(Brow)

        while (x+1 < self.size):
            B[x][y] = B[x+1][y] = B[x][y+1] = B[x+1][y+1] = 1
            x += 1
            y += 1

        x = 0
        y = 0
        while (x+1 < self.size):
            ret[x][y] = ret[x+1][y+1] = B
            ret[x+1][y] = ret[x][y+1] = I
            x += 1
            y += 1

        newRet = []
        for x in range(self.size):
            for y in range(self.size):
                col = []
                for z in range(self.size):
                    col += ret[x][z][y]
                newRet.append(col)

        ret = sympy.Matrix(newRet)

        return ret

    def getTransformations(self):
        self.setEndMatrix()

        #construct transformation matrix
        self.A = self.constructTransform()

        #get modular inverse of the matrix
        self.A = self.A.inv_mod(2)

        #obtain strategy x
        x = numpy.dot(numpy.subtract(self.b, self.p), self.A) % 2
        print("solution: ", x)
