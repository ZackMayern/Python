# Students of District College have subscriptions to English and French newspapers. 
# Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
# Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.



if __name__ == "__main__":
    n = input()
    eng = set(map(int, input().split()))
    
    b = input()
    french = set(map(int, input().split()))
    
    result = eng.symmetric_difference(french)
    print(len(result))