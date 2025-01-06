"""
solver from https://github.com/pmneila/Lights-Out/blob/master/lightsout.py
"""

import numpy
from operator import add
from itertools import chain, combinations
from functools import reduce

from plugins import Window, GalField, Util

class Solver:

    def __init__(self, size=5) -> None:
       self.size = size
       self.base = Util.lightsoutbase(self.size)
       self.inverseBase, self.null_vectors = Util.GF2inv(self.base)

    def solvable(self, config):
        arrConfig = numpy.asarray(config)
        assert arrConfig.shape[0] ==  arrConfig.shape[1] == self.size, "no"
        arrConfig = arrConfig.ravel()
        check = [numpy.dot(x, arrConfig) & 1 for x in self.null_vectors]
        return not any(check)

    def solve(self, config):
        arrConfig = numpy.asarray(config)
        assert arrConfig.shape[0] ==  arrConfig.shape[1] == self.size, "no"
        first = numpy.dot(self.inverseBase, config.ravel()) & 1
        solutions = [(first + reduce(add, nvs, 0)) & 1 for nvs in Util.powerset(self.null_vectors)]
        final = min(solutions, key=lambda x: x.sum())
        return numpy.reshape(final, (self.size, self.size))



