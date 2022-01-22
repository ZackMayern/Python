# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. 
# See the sample input/output for clarification. The first line contains the integer, n. The next n lines each contain a word. Output 2 lines.
# On the first line, output the number of distinct words from the input.On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

from collections import OrderedDict

if __name__ == "__main__":
    from collections import OrderedDict
    data = OrderedDict()
    
    for _ in range(int(input())):
        x = input()
        data[x]=data.get(x,0)+1
        
    print (len(data))
    print (" ".join(str(v) for k,v in data.items()))