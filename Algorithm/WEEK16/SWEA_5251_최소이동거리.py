for T in range(int(input())):
    N, E = map(int, input().split())
    arr = [0 for i in range(N+1)]
    se = {}
    for i in range(E):
        s, e, w = map(int, input().split())
        if not se.get(s):
            se[s] = {e: w}
        else:
            se[s][e] = w
        if not se.get(e):
            se[e] = {s: w}
        else:
            se[e][s] = w
    # print(se)
    group = [0] * (N + 1)
    group[0] = 1
    for _ in range(N):
        now_min = 1000
        for i in range(N+1):
            if group[i]:
                for k, v in se[i].items():
                    if not group[k]:
                        if v + arr[i] < now_min:
                            now_min = v + arr[i]
                            now_node = k
        arr[now_node] = now_min
        group[now_node] = 1
    print('#{} {}'.format(T+1, arr[N]))