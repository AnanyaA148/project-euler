temp =1
for i in range(100, 1000):
    for j in range(100, 1000):
            num = str( i *j)
            isPal = True
            for ch in range(len(num)):
                if num[ch] != num[-1-ch]:
                    isPal = False
            if isPal == True:
                if temp < i*j:
                    temp = i*j


print(temp)



