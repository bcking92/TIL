for T in range(int(input())):
    N, M = map(int,input().split())
    unbaked = list(map(int,input().split()))
    x = 1
    queue = []
    for i in range(N):
        queue.append([unbaked.pop(0), x])
        x += 1
    baked = []
    while queue:
        while len(queue) < N:
            if unbaked:
                queue.insert(0, [unbaked.pop(0), x])
                x += 1
            else:
                break
        a = queue.pop(0)
        a[0] //= 2
        if a[0]:
            queue.append(a)
        if len(queue) == 1:
            print('#{} {}'.format(T + 1, queue[0][1]))
            break
