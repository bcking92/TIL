def search(arr, x, temp, now):
    global candi, visited
    if x == N-1:
        candi.append(temp + arr[now][0])
    else:
        for i in range(1, N):
            if not visited[i]:
                visited[i] = 1
                search(arr, x+1, temp + arr[now][i], i)
                visited[i] = 0

for T in range(int(input())):
    N = int(input())
    arr = [tuple(map(int, input().split())) for i in range(N)]
    candi = []
    visited = [0] * N
    search(arr, 0, 0, 0)
    print('#{} {}'.format(T + 1, min(candi)))