for T in range(int(input())):
    arr, N = input().split()
    N = int(N)
    lll = len(arr)
    visited = {arr: 1}
    new_visited = {}
    now_max = 0
    for l in range(N):
        for k, v in visited.items():
            for i in range(lll):
                for j in range(i + 1, lll):
                    temp = list(k[:])
                    temp[i], temp[j] = temp[j], temp[i]
                    ddd = ''.join(temp)
                    if not new_visited.get(ddd):
                        new_visited[ddd] = 1
        visited = new_visited
        new_visited = {}
    for k, v in visited.items():
        if now_max < int(k):
            now_max = int(k)
    print('#{} {}'.format(T+1, now_max))
