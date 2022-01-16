# The first line contains integer T, the number of test cases.
# The next T lines contains the string S.
# Print "True" or "False" for each test case without quotes.
# Your task is to find out whether S is a valid regex or not.

import re

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        S = input()
        try:
            re.compile(S)
            print("True")
        except:
            print ("False")