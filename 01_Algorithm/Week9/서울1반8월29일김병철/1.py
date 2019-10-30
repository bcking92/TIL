for T in range(int(input())):
    N, M = map(int,input().split())
    queue = input().split()
    for i in range(M):
        queue.append(queue.pop(0))
    print('#{} {}'.format(T + 1, queue[0]))