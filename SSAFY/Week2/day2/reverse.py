# 1. problem.txt 파일을 생성 후, 다음과 같은 내용을 작성
0
1
2
3

# 2. problem.txt의 파일 내용을 다음과 같이 변경
3
2
1
0

# 3. problem.txt의 파일의 내용물을 역순으로 reverse.txt에 입력
0
1
2
3


# 1번


with open('problem.txt', 'w') as f :          
    a = [0,1,2,3]
    for i in a :
        f.writelines(str(i) + '\n')
  
with open('problem.txt', 'r') as f :

    pr = f.read()

    print(pr)
''' ----------------------------------------------------'''
# 2번


with open('problem.txt', 'w') as f :
    
    b = [3,2,1,0]
    for i in b :
        pr = f.write(str(i) + '\n')

with open('problem.txt', 'r') as f :

    pr = f.readlines()
    
    print(pr[0] + pr[1] + pr[2]+ pr[3])

'''-------------------------------------------------------'''

# # # 3번

with open('reverse.txt', 'w') as f :

    pr.reverse()
    
    for i in pr :
        pr1 = f.writelines(i)
        

with open('reverse.txt', 'r') as f :

    rev = f.read()

    print(rev)
