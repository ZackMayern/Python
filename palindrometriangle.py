#You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.
# 
# For example, a palindromic triangle of size 5 is:

# 1
# 121
# 12321
# 1234321
# 123454321
# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)**2) #the output is basically the square of quotient of (10^i/9)