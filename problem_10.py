import math
sum =0
for i in range(2, 2 * 10 **6):
    prime = True
    for j in range(2, int(math.sqrt(i))):
        if i % j ==0:
            prime = False
            break
    if prime:

        sum += i
print(sum)