# lotto API를 통해 최신 당첨번호를 가져온다.
import random
import requests
from flask import Flask


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
res = requests.get(url)
#json parsing = json file(str)을 python dictionary로 바꿈
dict_lotto = res.json()                  
json_lotto = res.text

# winner에 1등 당첨번호를 넣기
winner = []

for i in range(1,7) :
    winner.append(dict_lotto[f'drwtNo{i}'])

print(winner)

# 로또 랜덤 추천
your_lotto = sorted(random.sample(range(1,46),6))

# a = [1,1,1,1,1,1]
# try_lotto = 0
# third = 0
# try_third = 0
# while a != winner :
#     a = sorted(random.sample(list(range(1,46)),6))
#     gotit = 0
#     for i in range(6) :
#         for j in range(6) :
#             if a[j] == winner[i] :
#                 gotit += 1
#     try_lotto += 1
#     try_third += 1
#     if gotit == 5 :
#         print('{0}번만에 3등에 당첨되었습니다. \n당첨에 사용된 비용은 {1}원입니다.'.format(try_third,try_third*1000))
#         third += 1
#         try_third = 0
    
    

print('{0}번만에 1등에 당첨되었습니다.\n당첨에 사용된 비용은 {1}원입니다.\n1등에 당첨되는 동안 3등에 {2}번 당첨되었습니다.'.format(try_lotto,try_lotto*1000,third))


count = len(set(winner) & set(your_lotto))      
# for문 두번보다빠름
trial = 0
while true :
    if count == 6:
        print('갓등입니다')
        break
    trial += 1
    print(trial)

