a = int(input())
for i in range(a):
    b = input().split()
    N, K = int(b[0]),int(b[1])
    matrix = []
    num = 0

    for j in range(N):
        matrix.append(list(map(int,input().split())))
    
    matrix_90 = list(zip(*matrix[::-1]))
    matrix_180 = list(zip(*matrix_90[::-1]))
    matrix_270 = list(zip(*matrix_180[::-1]))

    for j in range(N):
        g = 0
        for k in range(N-K+1):
            if sum(matrix[j][k:k+K]) == K:
                matrix[j][k] = 0
                matrix[j][k+K-1] = 0
                num += 1

    for j in range(N):
        g = 0
        for k in range(N-K+1):
            if sum(matrix_270[j][k:k+K]) == K:
                matrix_270[j][k] = 0
                matrix_270[j][k+K-1] = 0
                num += 1
    print('#{} {}'.format(i+1,num))
        
