# You have to install numpy module for this.
# Two matrices are given input with NxN order and dot product is to be calculated

import numpy

if __name__ == "__main__":
    N = int(input())
    A = numpy.array([input().split() for i in range(N)],int)
    B = numpy.array([input().split() for i in range(N)],int)
    Result = numpy.dot(A.B)
    print(Result)