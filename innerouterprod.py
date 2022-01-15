# The first line contains the space separated elements of array A.
# The second line contains the space separated elements of array B.
# First, print the inner product.
# Second, print the outer product.

import numpy

if __name__ == "__main__":
    A = numpy.array([input().split()],int)
    B = numpy.array([input().split()],int)
    
    Inner = numpy.inner(A,B)
    Outer = numpy.outer(A,B)
    
    print(Inner[0,0])
    print(Outer)