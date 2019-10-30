for i in range(int(input())):
    N = int(input())
    matrix = []
    result = 0
    for j in range(10):
        matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for j in range(N):
        color = list(map(int,input().split()))
        for k in range(color[0],color[2]+1):
            for l in range(color[1],color[3]+1):
                matrix[k][l] += color[4]
    for j in range(10):
        for k in range(10):
            if matrix[j][k] == 3:
                result += 1
    print('#{} {}'.format(i+1,result))