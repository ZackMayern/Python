# Perform append, pop, popleft and appendleft methods on an empty deque d.
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.
# Print the space separated elements of deque d.

from collections import deque

if __name__ == "__main__":
    N = int(input())
    d = deque()
    
    for i in range(N):
        command = input().split()
        if command[0] == "append":
            d.append(command[1])
        if command[0] == "appendleft":
            d.appendleft(command[1])
        if command[0] == "pop":
            d.pop()
        if command[0] == "popleft":
            d.popleft()
    result = [str(i) for i in d]
    print(' '.join(result))