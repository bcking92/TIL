candy = 20
queue = [1]
i = 1

visit = {}
while candy > 0:
    tt = queue.pop(0)

    if visit.get(tt):
        visit[tt] += 1
    else:
        visit[tt] = 1
    candy -= visit[tt]
    print(tt, visit[tt], candy)
    queue.append(tt)
    i += 1
    queue.append(i)

print(visit)