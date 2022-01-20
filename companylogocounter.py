# A single line of input containing the string S. Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == "__main__":
    for i in Counter(sorted(input())).most_common(3):
        print(*i)