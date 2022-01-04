# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# Raghu is a shoe shop owner. His shop has x number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are n number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoes = Counter(map(int, input().split()))
    customer = int(input())
    earning = 0
    
    for i in range(customer):
        shoeNumber, price = map(int,(input()).split()) #Enter the size of the shoe and the price of the shoe
        if shoes[shoeNumber]:
            earning += price
            shoes[shoeNumber] -= 1
    
    print(earning)