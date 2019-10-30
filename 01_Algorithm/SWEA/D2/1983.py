from collections import OrderedDict

a = int(input())
scores=[1,2,3,4,5,6,7,8,9,10]
grades=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for i in range(a):
    grade = 0
    student_score = dict()
    N,K = map(int,input().split())
    for j in range(N):
        score = list(map(int,input().split()))
        student_score[j+1] = (score[0]*35 + score[1]*45 + score[2]*20)/100
    student_score = dict(OrderedDict(sorted(student_score.items(),key = lambda x : x[1])))

    rank = list(student_score.values()).index(student_score[K]) + 1
    for j in scores:
        if rank*10/N <= j:
            grade = grades[j-1]
    print('#{0} {1}'.format(i+1,grade))