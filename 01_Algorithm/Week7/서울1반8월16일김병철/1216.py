import sys

sys.stdin = open('input.txt', 'r')


def rotate_matrix(x):
    lenx = len(x)
    resultd = []
    for i in range(lenx):
        tem = ''
        for j in range(lenx):
            tem += x[j][i]
        resultd.append(tem)
    return resultd


def is_hoemoon(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True


def max_len_hoemoon(matrix, matrix2, k):
    for p in range(100):
        for l in range(k + 1):
            temp = matrix[p][l:l + 100 - k]
            temp2 = matrix2[p][l:l + 100 - k]
            if is_hoemoon(temp):
                return len(temp)
            if is_hoemoon(temp2):
                return len(temp2)
    return False


for i in range(10):
    input()
    matrix = []
    result = 0

    for j in range(100):
        matrix.append(input())

    rotated_matrix = rotate_matrix(matrix)

    for k in range(100):
        result = max_len_hoemoon(matrix, rotated_matrix, k)
        if result:
            break

    print('#{} {}'.format(i + 1, result))
