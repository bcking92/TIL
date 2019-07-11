'''
    Python dictionary 연습 문제
    '''
    
    # 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
    }

# 아래에 코드를 작성해 주세요.

#### 내가푼거
print('==== Q1 ====')
sum0 = 0 
for i in score :        
    sum0 += score[i]    
print(f'평균은{sum0/len(list(score.keys()))}점 입니다.')   

#### 갓동주님 코드
# print(sum(score.values()))
    
# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

#### 내가푼거
# sum1 = 0
# count = 0
# for st in scores :
#     for sb in scores[st] :
#         sum1 += scores[st][sb]
#         count += 1
# print(f'반 평균은 {sum1/count}입니다.')

#### 갓동주님 코드
sum3 = 0
for sb in scores :
    sum3 += sum(scores[sb].values())

print(sum3/len(scores.keys()))


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.


print('==== Q3-1 ====')
#### 갓동주님 코드
for temp in city.values():
    print(sum(temp)/len(temp))

#### 내가푼거
# for ct in city :
#     print(f'{ct}의 평균은 {sum(city[ct])/len(city[ct]):0.2}입니다.')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
#### 갓동주님 코드
maxes = []
mins = []
for temp in city.values():
    maxes.append(max(temp))
    mins.append(min(temp))

high = max(maxes)
low = min(mins)

for key, value in city.items():
    if high in value :
        print(f'{key}가 가장 더움')
    if low in value :
        print(f'{key}가 가장 추움')
print(max(maxes))
print(min(mins))

#### 내가푼거
# cold = {}
# hot = {}
# coldest = []
# hotest = []
# print('==== Q3-2 ====')
# for ct in city :
#     cold[ct] = min(city[ct])
#     coldest.append(cold[ct])
#     hot[ct] = max(city[ct])
#     hotest.append(hot[ct])
# for ct in city:
#     if cold[ct] == min(coldest):
#         print(f'{ct}시가 3일중 {min(coldest)}로 가장 추웠습니다.')
# for ct in city:
#     if hot[ct] == max(hotest):
#         print(f'{ct}시가 3일중 {max(hotest)}로 가장 더웠습니다.')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

             
# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

cityname = '서울'
temp = 2
for ct in city :
    if cityname == ct :
        if temp in city[ct] :
            print('있습니다')
        else :
            print('없습니다')

#### 갓동주님 코드