from collections import Counter

x =int(input())
shoe_sizes  = list(map(int, input().split()))
stock = Counter(shoes_size) 
n = int(input())

earnings = 0 
for i in range(n):
    size, price = map(int, input().split())
    if stock[size] > 0:
        earnings += price
        stock[size] -= 1


print(earnings)


