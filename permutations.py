# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

from itertools import permutations

if __name__ == '__main__':
    s, k = input().split(maxsplit=1) #takes string and int as inputs
    output = ["".join(i) for i in permutations(s, int(k))] #specifies k as int since input taken is stored as str type
    output.sort() #sorts list in alphabetical order
    print("\n".join(output))