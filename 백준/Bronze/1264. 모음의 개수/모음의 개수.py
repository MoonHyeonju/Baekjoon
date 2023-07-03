while True:
    count = 0 
    s = input()
    if s == '#':
        break
       
    for i in s:
        if i in 'AaEeIiOoUu':
            count += 1       
    print(count)