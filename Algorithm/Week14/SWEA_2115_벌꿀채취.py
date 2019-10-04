for T in range(int(input())):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N**2):
        if (i % N) < N - M + 1:
            for j in range(i+1, N**2):
                now_max = [0, 0]
                if j - i >= M and (j % N) < N - M + 1:
                    temp_i = [0, 0]
                    temp_j = [0, 0]
                    temp_i[0], temp_i[1] = i//N, j//N
                    temp_j[0], temp_j[1] = i % N, j % N
                    for k in range(2):
                        temp = honey[temp_i[k]][temp_j[k]:temp_j[k] + M]
                        if sum(temp) <= C:
                            temp_max = 0
                            for l in temp:
                                temp_max += l ** 2
                            now_max[k] = temp_max
                        else:
                            for l in range(1, 2 ** M):
                                temp_num = 0
                                temp_max = 0
                                for n in range(l):
                                    if l & (1 << n):
                                        temp_num += temp[n]
                                        temp_max += temp[n] ** 2
                                if temp_num <= C:
                                    if temp_max > now_max[k]:
                                        now_max[k] = temp_max
                    temp_result = now_max[0] + now_max[1]
                    if temp_result > result:
                        result = temp_result
    print('#{} {}'.format(T+1, result))