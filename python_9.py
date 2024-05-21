find = False
for i in range(1000):
    for j in range (i):
        if i**2 + j**2 == (1000-i-j) **2:
            print(i*j*(1000-i-j))
            find = True
            break
    if find:
        break