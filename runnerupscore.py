# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the 
# runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr.sort()
    
    max = arr[0]
    secondrunner = arr[0]
    
    for i in range (1,n):
        if arr[i]>max:
            max = arr[i]
    for j in range (1,n):
        if arr[j]<max:
            secondrunner = arr[j]
    print(secondrunner)
