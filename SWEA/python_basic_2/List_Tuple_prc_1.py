List_Score = [(90, 80),(85, 75),(90, 100)]

for stnum in range(len(List_Score)) :
    print('{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1F}입니다.'.format(stnum+1,sum(List_Score[stnum]),sum(List_Score[stnum])/len(List_Score[stnum])))
