# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())

for string in range (1 , n+1):
    print(string, end="")
