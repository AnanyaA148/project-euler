num =20
paths =1
for i in range(num+1, 2*num +1):
    paths *= i
    paths = paths/ (i-num)
print(paths)