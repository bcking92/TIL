dic = {
   0: [1, 2, 3],
   1: [4, 5, 6],
   2: [7, 8, 9],
   3: [10, 11, 12],
}

arr = [i for i in range(7)]

def bfs(x):
    global result
    depth = 1
    queue = []
    queue.append([x])
    cnt = 0
    while queue:
        cnt += 1
        t = queue.pop(0)
        result.append(t)
        print('depth : {}'.format(depth), *result)
        for i in arr:
            queue.append(result[-1] + [i])
        result.pop()
        if len(queue) >= 7 ** depth:
            depth += 1
        if depth > 6:
            break
    print(cnt)

result = []

bfs(0)