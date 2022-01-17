# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.

from collections import OrderedDict

if __name__ == "__main__":
    N = input()
    data = OrderedDict()
    for i in range(int(N)):
        item, name, price = input().rpartition(' ')
        data[item] = data.get(item, 0) + int(price)
    for item, price in data.items():
        print(item, price)