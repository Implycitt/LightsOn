import numpy, sympy

class Solve:

    def getTransformations(self):
        p = numpy.array([1, 0, 0, 1])
        b = numpy.array([1, 1, 1, 1])
        A = sympy.Matrix([[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]])
        A = A.inv_mod(2)

        x = numpy.dot(numpy.subtract(b, p), A) % 2
        print(x)

if __name__ == '__main__':
    s = Solve()
    s.getTransformations()
