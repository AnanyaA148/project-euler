num =2
count = 1
while(count < 10001):
    prime = False
    num = num+1
    for i in range(2, num):
        if num % i ==0:
            prime = False
            break
        else:

            prime = True

    if prime:
        count = count +1

print(num)

