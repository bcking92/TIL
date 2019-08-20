hoobo = [1 for i in range(0,1000)]

for i in range(101):
    hoobo[i] = 0
for i in range(101,1000):
    if len(set(str(i))) != 3:
        hoobo[i] = 0
    if '0' in str(i):
        hoobo[i] = 0
    
for i in range(int(input())):
    young, strike, ball = map(int,input().split())
    if strike != 3:
        hoobo[young] = 0
        for j in range(101,1000):
            if len(set(str(young)) & set(str(j))) != strike + ball:
                hoobo[j] = 0
            cnt = 0
            for k in range(3):
                if str(young)[k] == str(j)[k]:
                    cnt += 1
            if cnt != strike:
                hoobo[j] = 0
    else:
        result = 1
        break
    result = sum(hoobo)
print(result)






