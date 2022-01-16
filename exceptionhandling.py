# You are given two values a and b.
# Perform integer division and print a/b.
# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b.

if __name__ == "__main__":
    N = int(input())
    for i in range (N):
        A, B = input().split()
        
        try:
            quotient = int(A)//int(B)
            print(quotient)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except BaseException as e:
            print("Error Code:", e)