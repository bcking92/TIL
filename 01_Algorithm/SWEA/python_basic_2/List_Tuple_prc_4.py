List_1 = []
for i in range(5) :
    List_1.append(int(input()))

print('입력된 값 {0}의 평균은 {1:0.1F}입니다.'.format(str(List_1), sum(List_1)/len(List_1)))
