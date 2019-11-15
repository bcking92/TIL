import sys

sys.stdin = open('sample_input.txt', 'r')

for T in range(int(input())):
    if T != 4:
        N = int(input())
        arr = [tuple(map(int, input().split())) for i in range(N)]
        continue
    N = int(input())
    result = -1
    my_max = 0
    arr = [tuple(map(int, input().split())) for i in range(N)]
    for i in range(1, N-1):
        for j in range(i):
            a = (i - j, j)
            # print(f'a = {arr[i-j][j]}')
            for k in range(i-j):
                b = (i - j - (1 + k), j + (1 + k))
                # print(f'b = {arr[i - j - (1 + k)][j + (1 + k)]}')

                for l in range(min(N - (i - j + 1), N - (j + (1 + k) + 1))):
                    # print(N)
                    # print(N - (i - j + 1))

                    # print(N - (j + (1 + k) + 1))
                    # print(min(N - (i - j + 1), N - (j + (1 + k) + 1)))
                    # print(k + 2 , l + 2)
                    go = 1
                    # print(f'c = {arr[i - j + 1 + l][j + 1 + l]}')
                    # print(f'd = {arr[i - j - (1 + k) + l + 1][j + (1 + k) + l + 1]}')
                    # print('---')
                    c = (i - j + 1 + l, j + 1 + l)
                    d = (i - j - (1 + k) + l + 1, j + (1 + k) + l + 1)
                    print(f'a = {a}, b = {b}, c = {c}, d = {d}')
                    visited = {}
                    temp = 0
                    for m in range(k+2):
                        if not visited.get(arr[i - j - m][j + m]):
                            visited[arr[i - j - m][j + m]] = 1
                            temp += arr[i - j - m][j + m]
                        else:
                            go = 0
                            break
                        if not visited.get(arr[i - j + 1 + l - m][j + 1 + l + m]):
                            visited[arr[i - j + 1 + l - m][j + 1 + l + m]] = 1
                            temp += arr[i - j + 1 + l - m][j + 1 + l + m]
                        else:
                            go = 0
                            break
                    if go:
                        for n in range(1, l+1):
                            if not visited.get(arr[i - j + l][j + l]):
                                visited[arr[i - j + l][j + l]] = 1
                                temp += arr[i - j + l][j + l]
                            else:
                                go = 0
                                break
                            b = (i - j - (1 + k), j + (1 + k))
                            if not visited.get(arr[i - j - (1 + k) + l][j + (1 + k) + l]):
                                visited[arr[i - j - (1 + k) + l][j + (1 + k) + l]] = 1
                                temp += arr[i - j - (1 + k) + l][j + (1 + k) + l]
                            else:
                                go = 0
                                break
                    if go:
                        if temp > my_max:
                            my_max = temp
                            result = (l + 2) * (k + 2)
    print('------')
    print(result)