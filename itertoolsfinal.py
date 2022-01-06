# The input consists of three lines. The first line contains the integer n, denoting the length of the list. 
# The next line consists of n space-separated lowercase English letters, denoting the elements of the list.
# The third and the last line of input contains the integer k, denoting the number of indices to be selected.

# Output a single line consisting of the probability that at least one of the k indices selected contains the letter: 'a'.

from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    s = input().split(' ')
    k = int(input())
    
    counter = 0
    length = 0
    
    for c in combinations(s,k):
        length += 1
        if "a" in c:
            counter += 1
                
    print (float(counter/length))