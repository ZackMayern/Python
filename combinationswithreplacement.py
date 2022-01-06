# You are given a string .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
# THe only difference is that the output will have repeating set of indexes

from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, k = input().split()
    listA = ["".join(i) for i in s]
    listA.sort()
    output = ["".join(i) for i in combinations_with_replacement(listA,int(k))]
    print("\n".join(output))