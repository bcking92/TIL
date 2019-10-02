def dfs(x):
    global visited
    if link.get(x):
        for i in link[x]:
            if not visited[i]:
                visited[i] = 1
                dfs(i)

for T in range(int(input())):
    N, M = map(int, input().split())
    visited = [0] * 101
    link = {}
    cnt = 0
    for i in range(M):
        a, b = map(int, input().split())
        if not link.get(a):
            link[a] = [b]
        else:
            link[a].append(b)
        if not link.get(b):
            link[b] = [a]
        else:
            link[b].append(a)
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print('#{} {}'.format(T+1, cnt))