check =0
count = 0
num =1
while(check < 500 ):
    check =0
    count +=1
    num = count *(count+1)//2

    for i in range(num):
        if num % (i+1) ==0:
            check +=1

print(num)
