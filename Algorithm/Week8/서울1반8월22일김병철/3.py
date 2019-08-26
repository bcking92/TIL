def dfs(linked_list, start):
    if not visited[start]:
        visited[start] = 1
        sub.append(start)
        for i in linked_list[start]:
            dfs(linked_list, i)

for T in range(int(input())):
    V, E = map(int,input().split())
    visited = [ 0 for i in range(V+1)]
    node = [ [0] for i in range(V+1)]
    sub = []
    for i in range(E):
        a, b = map(int,input().split())
        node[a].append(b)
    c, d = map(int,input().split())
    dfs(node, c)
    if d in sub:
        print('#{} {}'.format(T+1, 1))
    else:
        print('#{} {}'.format(T+1, 0))