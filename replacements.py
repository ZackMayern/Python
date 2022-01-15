# You are given a string s.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order. A single line containing the string s and integer value k separated by a space.
# Print the combinations with their replacements of string s on separate lines.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, k = input().split()
    listA = ["".join(i) for i in s]
    listA.sort()
    output = ["".join(i) for i in combinations_with_replacement(listA,int(k))]
    print("\n".join(output))