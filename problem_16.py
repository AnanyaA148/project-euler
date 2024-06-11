n =1000
num = 2**n
sum = 0
while(num > 0):
    sum += (num%10)
    num = int(num/10)
print(sum)