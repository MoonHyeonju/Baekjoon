L, p = map(int, input().split())
n = list(map(int, input().split()))

for i in range(5):
    print(n[i] - L * p, end=' ')