for T in range(int(input())):
    V, E = map(int, input().split())
    nodes = tuple([{} for i in range(V+1)])
    result = 0
    fail = 0
    for i in range(E):
        a, b, w = map(int, input().split())
        nodes[a][b] = w
        nodes[b][a] = w
    group = [0] * (V + 1)
    group[0] = 1
    while sum(group) != V+1:
        now_min = 11
        now_node = -1
        for i in range(V+1):
            if group[i]:
                for j, w in nodes[i].items():
                    if not group[j]:
                        if now_min > w:
                            now_min = w
                            now_node = j
        group[now_node] = 1
        result += now_min
    if not fail:
        print('#{} {}'.format(T+1, result))

