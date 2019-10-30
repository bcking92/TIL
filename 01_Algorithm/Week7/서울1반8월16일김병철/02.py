def rotate_matrix(x):
    lenx = len(x)
    resultd = []
    for i in range(lenx):
        d = []
        for j in range(lenx):
            d.append(0)
        resultd.append(d)
    for i in range(lenx):
        for j in range(lenx):
            resultd[j][i] = x[i][j]
    return resultd

for i in range(int(input())):
    N, M = list(map(int,input().split()))
    result = ''
    matrix = []
    for j in range(N):
        matrix.append(list(input()))
    for j in range(N):
        if result :
            break
        for k in range(N-M+1):
            temp = matrix[j][k:k+M]
            if temp == temp[::-1]:
                result = temp
                break
    for j in range(N):
        if result :
            break
        for k in range(N-M+1):
            temp = rotate_matrix(matrix)[j][k:k+M]
            if temp == temp[::-1]:
                result = temp
                break
    print('#{} {}'.format(i+1, ''.join(result)))
