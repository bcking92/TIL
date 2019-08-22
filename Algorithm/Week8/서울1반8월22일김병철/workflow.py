import sys

sys.stdin = open('input.txt', 'r')

# def dfs(x):
#     for i in priority[x]:
#         if not visited[i]:
#             dfs(i)
#     else:
#         if not visited[x]:
#             visited[x] = 1
#             print(x, end=' ')
#             for j in link_neighbor[x]:
#                 if not visited[j]:
#                     dfs(j)
#             else:
#                 for k in range(1,V+1):
#                     if not visited[k]:
#                         dfs(k)
#         else:
#             pass
# dfs(lines[0])

for T in range(10):
    print('#{}'.format(T + 1), end=' ')
    V, E = map(int, input().split())
    lines = list(map(int, input().split()))
    link_neighbor = [[] for i in range(V + 1)]
    priority = [[] for i in range(V + 1)]
    visited = [0 for i in range(V + 1)]
    for i in range(0, len(lines), 2):
        link_neighbor[lines[i]].append(lines[i + 1])
        link_neighbor[lines[i+1]].append(lines[i])
        priority[lines[i + 1]].append(lines[i])
    now = lines[0]
    while sum(visited) <= V-1:
        for j in priority[now]:
            if not visited[j]:
                now = j
                break
        else:
            if not visited[now]:
                visited[now] = 1
                print(now, end=' ')
                for k in link_neighbor[now]:
                    if not visited[k]:
                        now = k
                        break
                else:
                    for l in range(1, V+1):
                        if not visited[l]:
                            now = l
                            break
    print()
