price = [int(input()) for _ in range(5)]

result = min(price[0:3]) + min(price[3:5]) - 50

print(result)