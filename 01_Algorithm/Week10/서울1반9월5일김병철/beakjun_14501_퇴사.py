# BJ14501
# from sys import setrecursionlimit
#
# setrecursionlimit(10 ** 6)


def combi():
    global result, temp, days_left
    for i in range(N - days_left, N):
        go = 0
        if not visited[i]:
            if Tn[i] > days_left:
                if result < temp:
                    result = temp
                    return
                else:
                    return
            else:
                go = 1
                break
    if go:
        for i in range(N):
            if not visited[i]:
                if Tn[i] <= N - i:
                    for j in range(Tn[i]):
                        if i + j < N:
                            visited[i + j] = 1
                        else:
                            break
                    temp += Pn[i]
                    days_left -= Tn[i]
                    combi()
                    temp -= Pn[i]
                    days_left = N - i - Tn[i]
                    for j in range(Tn[i]):
                        if i + j < N:
                            visited[i + j] = 0
                        else:
                            break

N = int(input())
Tn = []
Pn = []
visited = [0 for i in range(N)]
result = 0
temp = 0
days_left = N
for _ in range(N):
    T, P = map(int, input().split())
    Tn.append(T)
    Pn.append(P)

combi()

print(result)




