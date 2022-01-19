# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
# Output the symmetric difference integers in ascending order, one per line.

if __name__ == "__main__":
    M = input()
    # for 'A' input
    a = input().strip().split()
    setA = set(map(int, a))
    
    N = input()
    # for 'B' input
    b = input().strip().split()
    setB = set(map(int, b))
    
    l = sorted((setA.difference(setB)).union(setB.difference(setA)))
    print('\n'.join([str(ele) for ele in l]))