key = [
    [1,2,3]
   ,[4,5,6]
   ,[7,8,9]
    ]



for i in range(3):
    print(key[i])



key = list(zip(*key[::-1])) # 돌리는 부분 <- 이렇게하면 90도 돌아 매트릭스가
key = list(zip(*key[::-1])) # 돌리는 부분 <- 이렇게하면 90도 돌아 매트릭스가


print()
for i in range(3):
    print(key[i])
