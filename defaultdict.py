# Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

# For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A, so print -1.

from collections import defaultdict

if __name__ == '__main__':
    default = defaultdict(list)
    n, m = map(int, input().split())
    for i in range(n):
        default[input()].append(str(i+1))
        
    for j in range(m):
        print(' '.join(default[input()]) or -1)