n = int(input())

for _ in range(n):
    x = list(input())
    score = 0
    sum = 0
    for i in x:
        if i == "O":
            score += 1
        else:
            score = 0
        sum += score
    print(sum)