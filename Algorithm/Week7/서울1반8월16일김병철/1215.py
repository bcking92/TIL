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

for i in range(10):
    N = int(input())
    matrix = []
    result = 0
    for j in range(8):
        matrix.append(list(input()))
    for j in range(8):
        for k in range(9-N):
            temp = matrix[j][k:k + N]
            temp2 = rotate_matrix(matrix)[j][k:k + N]
            if temp == temp[::-1]:
                result += 1
            if temp2 == temp2[::-1]:
                result += 1
    print('#{} {}'.format(i + 1, result))