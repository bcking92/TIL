for T in range(int(input())):
    cost = tuple(map(int, input().split()))
    time = (0, 0, 2, 11)
    plan = tuple(map(int, input().split()))
    stack = [(0, 0)]
    for i in range(12):
        if plan[i]:
            new = []
            for c, time_left in stack:
                if not time_left:
                    for j in range(4):
                        if not j:
                            new.append((c + cost[j] * plan[i], 0))
                        else:
                            new.append((c + cost[j], time[j]))
                else:
                    new.append((c, time_left-1))
            stack = new
    print('#{} {}'.format(T+1, sorted(stack)[0][0]))
