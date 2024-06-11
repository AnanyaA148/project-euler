import math
num = 600851475143
root1 = int(math.sqrt(num))

count = 2
temp =1
while (count <= root1):
    if num % count == 0:
        num = num / count
        temp = count
    else:
        count = count + 1

print(temp)
