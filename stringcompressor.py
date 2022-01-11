# A single line of input consisting of the string s. A single line of output consisting of the modified string. 
# First, the character 1 occurs only once. It is replaced by (1,1). Then the character 2 occurs three times, and it is replaced by (3,2) and so on.
# Also, note the single space within each compression and between the compressions.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == '__main__':
    s = input()
    for key, group in groupby(s):
        key = int(key)
        count = len(list(group))
        print((count, key), end=" ") 