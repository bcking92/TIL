import collections
deque = collections.deque

def shuffle(a, n):
    global N
    shuffled_card = a.copy()
    if n < N//2:
        for i in range(n):
            for j in range(i+1):
                shuffled_card[N//2 - 1 - i + 2 * j], shuffled_card[N//2 - i + 2 * j] = shuffled_card[N//2 - i + 2 * j], shuffled_card[N//2 - 1 - i + 2 * j]
        return shuffled_card
    else:
        for i in range(N//2):
            shuffled_card[i], shuffled_card[i+N//2] = shuffled_card[i + N//2], shuffled_card[i]
        if n == N-1:
            return shuffled_card
        else:
            for i in range(N-1-n):
                for j in range(i+1):
                    shuffled_card[N // 2 - 1 - i + 2 * j], shuffled_card[N // 2 - i + 2 * j] = shuffled_card[N // 2 - i + 2 * j], shuffled_card[N // 2 - 1 - i + 2 * j]
            return shuffled_card

def bfs(x):
    global N
    cards = list(map(int, input().split()))
    global T
    queue = deque([])
    queue.append([cards, 0, 0])
    while queue:
        t = queue.popleft()
        v = t[0]
        d = t[1]
        if v == sorted(v) or v == sorted(v, reverse=True):
            print('#{} {}'.format(T+1, d))
            return
        if d < 6:
            for i in range(1, N):
                if t[2] == i:
                    if i == 1:
                        continue
                    elif i == N-1:
                        continue
                    elif i == N-2:
                        continue
                    else:
                        queue.append([shuffle(v, i), d+1, i])
                else:
                    queue.append([shuffle(v, i), d+1, i])
    print('#{} {}'.format(T+1, -1))
    return


for T in range(int(input())):
    N = int(input())
    bfs(0)


