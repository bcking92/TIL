def bfs(s, d):
    global ll
    global T
    queue = [(s, 0)]
    visited = {}
    while queue:
        temp = queue.pop(0)
        visited[temp[0]] = 1
        if temp[0] == d:
            print('#{} {}'.format(T+1, temp[1]))
            return
        if ll[temp[0]]:
            for j in ll[temp[0]]:
                if not visited.get(j):
                    queue.append((j, temp[1] + 1))
    print('#{} {}'.format(T+1, 'impossible'))

for T in range(int(input())):
    V, E = map(int, input().split())
    ll = [[] for i in range(V+1)]
    for i in range(E):
        link = tuple(map(int, input().split()))
        ll[link[0]].append(link[1])
        ll[link[1]].append(link[0])
    S, G = map(int, input().split())
    bfs(S, G)