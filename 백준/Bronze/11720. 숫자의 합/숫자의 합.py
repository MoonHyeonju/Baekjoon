n = int(input())
data = int(input())
sum = 0

while data != 0:
    sum += data % 10

    data //= 10

print(sum)