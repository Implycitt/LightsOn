"""
utils from https://github.com/pmneila/Lights-Out/blob/master/lightsout.py
"""
import numpy
from operator import add
from itertools import chain, combinations
from scipy import ndimage
from functools import reduce
from plugins import Window, GalField

GF2array = numpy.vectorize(GalField.GaloisField2)

def gjel(A):
    nulldim = 0
    for i, row1 in enumerate(A):
        pivot = A[i:, i].argmax() + i
        if A[pivot, i] == 0:
            nulldim = len(A) - i
            break
        new_row = A[pivot] / A[pivot, i]
        A[pivot] = A[i]
        row1[:] = new_row
        
        for j, row2 in enumerate(A):
            if j == i:
                continue
            row2[:] -= new_row*A[j, i]
    return A, nulldim


def GF2inv(A):
    n = len(A)
    assert n == A.shape[1], "Matrix must be square"
    A = numpy.hstack([A, numpy.eye(n)])
    B, nulldim = gjel(GF2array(A))
    inverse = numpy.int_(B[-n:, -n:])
    E = B[:n, :n]
    null_vectors = []
    if nulldim > 0:
        null_vectors = E[:, -nulldim:]
        null_vectors[-nulldim:, :] = GF2array(numpy.eye(nulldim))
        null_vectors = numpy.int_(null_vectors.T)
    return inverse, null_vectors

def lightsoutbase(n):
    a = numpy.eye(n*n)
    a = numpy.reshape(a, (n*n, n, n))
    a = numpy.array(list(map(ndimage.binary_dilation, a)))
    return numpy.reshape(a, (n*n, n*n))

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

