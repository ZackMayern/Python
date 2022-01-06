# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

from itertools import groupby

if __name__ == '__main__':
    s = input()
    for key, group in groupby(s):
        key = int(key)
        count = len(list(group))
        print((count, key), end=" ") 