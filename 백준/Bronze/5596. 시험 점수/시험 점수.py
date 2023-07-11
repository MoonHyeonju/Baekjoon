a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

s = a + b + c + d
t = e + f + g + h

if s >= t:
    print(s)
else:
    print(t)