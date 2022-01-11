# s = "AAABCADDE" and k = 3
# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1 = 'A'. The second substring has all distinct characters, 
# so u2 = 'BCA'. The third substring has 2 different characters, so u3 = 'DE'. Note that a subsequence maintains the original order of characters encountered. 
# The order of characters in each subsequence shown is important.

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        split = string[i:i+k]
        l = ""
        for i in split:
            if i not in l:
                l += i
        print(l)