from collections import deque

for T in range(int(input())):
    N, M = map(int, input().split())
    # print(N, M)
    queue = deque()
    result = 0
    queue.append(N)
    memo = [0] * 1000001
    while queue:
        now = queue.popleft()
        d = memo[now]
        if now == M:
            result = d
            break
        else:
            if 0 <= now + 1 <= 1000000:
                if not memo[now+1]:
                    queue.append(now+1)
                    memo[now + 1] = d + 1
            if 0 <= now - 1 <= 1000000:
                if not memo[now-1]:
                    queue.append(now-1)
                    memo[now - 1] = d + 1
            if 0 <= now * 2 <= 1000000:
                if not memo[now*2]:
                    queue.append(now*2)
                    memo[now * 2] = d + 1
            if 0 <= now - 10 <= 1000000:
                if not memo[now-10]:
                    queue.append(now-10)
                    memo[now - 10] = d + 1

    print('#{} {}'.format(T+1, result))