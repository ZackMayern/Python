# Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
# Your task is to help Dr. Wesley calculate the average marks of the students.

from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    Data = namedtuple('Data',input().split())
    scores = [Data(*input().split()).MARKS for i in range(n)]
    print("%.2f"% (sum(map(int,scores))/n))