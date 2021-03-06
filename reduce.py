# First line contains n, the number of rational numbers.
# The ith of next n lines contain two integers each, the numerator(Ni) and denominator(Di) of the ith rational number in the list. 
# Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, 
# i.e. numerator and denominator have no common divisor other than 1.

from fractions import Fraction
from functools import reduce

import operator

def product(fracs):
    t = reduce(operator.mul, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)