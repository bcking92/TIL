result = []
for i in range(2,10) :
    dan = []
    for j in range(1,10) :
        if i * j % 3 != 0 and i * j % 7 != 0 :
            dan.append(i*j)
    result.append(dan)

print(result)            

