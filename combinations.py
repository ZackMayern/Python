# You are given a string .
# Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    listA = ["".join(i) for i in s] #amking a list where input is separated and will be sorted in alphabetical order
    listA.sort()
    
    for j in range(1,int(k)+1):
        output = ["".join(i) for i in combinations(listA, j)] #makes combination and stores in output as list format
        #output.sort() this line is not needing since the list is already sorted alphabetically wise
        print("\n".join(output))