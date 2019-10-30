def solution(A,B):
    answer = 0
    candi1 = []
    candi2 = []
    permu_index = []
    stack = [[]]
    while stack:
        t = stack.pop()
        if len(t) == len(A):
            permu_index.append(t)
        else:
            for i in [j for j in range(len(A))]:
                if i not in t:
                    stack.append(t + [i])
    print(permu_index)

solution([1,2,3],[4,5,6])