check =0
count = 1
num =1
while(check < 500 ):
    check =0
    count +=1
    num += count

    for i in range(num):
        if num % (i+1) ==0:
            check +=1
print(num)
