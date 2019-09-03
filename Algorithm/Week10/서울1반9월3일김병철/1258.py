for T in range(int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for i in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                dy = 1
                dx = 1
                if 0 <= j + dy < n:
                    while matrix[i][j + dy]:
                        dy += 1
                        if not 0 <= j + dy < n:
                            break
                if 0 <= i + dx < n:
                    while matrix[i + dx][j]:
                        dx += 1
                        if not 0 <= i + dx < n:
                            break
                for k in range(i, i + dx):
                    for l in range(j, j+ dy):
                        matrix[k][l] = 0
                result.append([dx, dy])
                # 정렬 우선순위는 튜플로 줄 수 있음!! 개꿀맛
    result = sorted(result, key=lambda x : (x[0] * x[1], x[0]))
    print('#{} {} {}'.format(T + 1, len(result), str(result).replace('[', '').replace(']', '').replace(',', '')))