N, M, K, X = map(int, input().split())

# cost = [9999999 for i in range(N+1)]
visited = [0 for i in range(N+1)]
road = {}
distances = {}
distances[0] = [X]
visited[X] = 1

for i in range(M):
    a, b = map(int, input().split())
    if not road.get(a):
        road[a] = [b]
    else:
        road[a].append(b)

for i in range(K+1):
    if distances.get(i):
        for node in distances[i]:
            if road.get(node):
                for next_node in road[node]:
                    if not visited[next_node]:
                        if not distances.get(i+1):
                            distances[i+1] = [next_node]
                            visited[next_node] = 1
                        else:
                            distances[i+1].append(next_node)
                            visited[next_node] = 1

if distances.get(K):
    for node in sorted(distances[K]):
        print(node)
else:
    print(-1)

# def my_min():
#     now_min = 9999999
#     result = -1
#     for i in range(N):
#         if not visited[i] and now_min > cost[i]:
#             now_min = cost[i]
#             result = i
#     return result

# for i in range(M):
#     a, b = map(int, input().split())
#     if not road.get(a):
#         road[a] = [b]
#     else:
#         road[a].append(b)

# cost[X] = 0
# for i in range(N):
#     now = my_min()
#     visited[now] = 1
#     if now != -1 and road.get(now):
#         for node in road.get(now):
#             if cost[node] > cost[now] + 1:
#                 cost[node] = cost[now] + 1

# exist = False        
# for i in range(N+1):
#     if cost[i] == K:
#         exist = True
#         print(i)

# if not exist:
#     print(-1)


# if distances.get(K):
#     for i in distances[K]:
#         print(i)
# else:
#     print(-1)

# def bfs(start, road):
#     minimal = [99999999 for i in range(N+1)]
#     visited = [0 for i in range(N+1)]
#     queue = [(start,0)]
#     while True:
#         if not queue:
#             break
#         now, cost = queue.pop(0)
#         visited[now] = 1
#         if cost > K:
#             break
#         if minimal[now] > cost:
#             minimal[now] = cost
#         if road.get(now):
#             for node in road.get(now):
#                 if not visited[node]:
#                     queue.append((node, cost+1))
#     return minimal
        
# not_exist = True
# for idx, i in enumerate(bfs(X, road)):
#     if (i == K):
#         not_exist = False
#         print(idx)
# if not_exist:
#     print(-1)

