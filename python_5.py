count = 1
done = False
while not done:
    count = count + 1
    for i in range(20):
        if count % (i+1) != 0:
            done = False
            break
        else:
            done = True
print(count)