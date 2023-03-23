day = int(input())
n = list(map(int, input().split()))
count = 0
for i in n:
    if i == day:
        count += 1

print(count)