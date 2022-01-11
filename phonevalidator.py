# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
# Regular expressions are a key concept in any programming language.

import re
if __name__ == '__main__':
    s = input()
    for i in range(int(s)):
        a = input()
        if re.match(r'^[789]\d{9}$', a):
            print("YES")
        else:
            print("NO")