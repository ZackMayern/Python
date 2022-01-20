# The first line contains a single integer T, the number of test cases.
# For each test case, there are 2 lines.
# The first line of each test case contains n, the number of cubes.
# The second line contains n space separated integers, denoting the sideLengths of each cube in that order.
# For each test case, output a single line containing either Yes or No.

from collections import deque

if __name__ == "__main__":
    def check(cube):
        while cube:
            big = cube.popleft() if cube[0]>cube[-1] else cube.pop()
            if not cube:
                return "Yes"
            if cube[-1]>big or cube[0]>big:
                return "No"
    
    for i in range(int(input())):
        int(input())
        cube = deque(map(int,input().split()))
        print(check(cube))