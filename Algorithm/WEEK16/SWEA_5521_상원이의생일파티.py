for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [[] for i in range(N+1)]
    visited = [0 for i in range(N+1)]
    result = 0
    visited[1] = 1
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in arr[1]:
        for j in arr[i]:
            if not visited[j]:
                visited[j] = 1
    result = sum(visited) - 1
    print('#{} {}'.format(T+1, result))