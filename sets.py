# The first line contains integers n and m separated by a space. 
# The second line contains n integers, the elements of the array. 
# The third and fourth lines contain m integers, A and B, respectively. 
# Output a single integer, your total happiness.

if __name__ == "__main__":
    n, m = input().split()
    happiness = 0

    sets = list(map(int, input().strip().split()))

    A = set(map(int, input().strip().split()))
    B = set(map(int, input().strip().split()))

    for i in sets:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1
    print(happiness)