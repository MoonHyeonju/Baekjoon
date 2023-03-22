a, b = map(int, input().split())

d = a * (100 - b) * 0.01

if d >= 100:
    print("0")
else:
    print("1")