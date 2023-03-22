n = int(input())

for i in range(n):
    pwd = input()
    if 6 <= len(pwd) <= 9:
        print("yes")
    else:
        print("no")