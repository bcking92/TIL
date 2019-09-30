def select(x):
    global result, temp, heights, end
    if not end:
        if x <= N:
            if B < temp:
                if temp < result:
                    result = temp
            elif B == temp:
                result = temp
                end = 1
            else:
                if x < N:
                    temp += heights[x]
                    select(x + 1)
                    temp -= heights[x]
                    select(x + 1)


for T in range(int(input())):
    N, B = map(int, input().split())
    end = 0
    heights = sorted(list(map(int, input().split())))
    result = 100000
    temp = 0
    select(0)
    print('#{} {}'.format(T + 1, result - B))