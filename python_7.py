import math
lst = [2]
check =1
num =2
count = 1
while(count < 10001):
    prime = False
    num = num+1
    i = 0
    for check in lst:
        if check < math.sqrt(num):
            if num % check ==0:
                prime = False
                break
            else:
                prime = True
            i = i+1


    if prime:
        count = count +1
        lst.append(num)

print(num)

