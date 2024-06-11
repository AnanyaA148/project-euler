count = 1
num = count
done = False
track =1
while not done:
    count = count + num
    for i in range(20):
        if count % (i+1) != 0:
            done = False
            if i > track:
                track = i+1
                num = count
            break
        else:
            done = True
print(count)