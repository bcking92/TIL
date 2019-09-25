for T in range(int(input())):
    M, N = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    visited = [0] * len(containers)
    result = 0
    for i in trucks:
        for j in range(len(containers)):
            if i >= containers[j]:
                if not visited[j]:
                    visited[j] = 1
                    result += containers[j]
                    break
    print('#{} {}'.format(T + 1, result))
