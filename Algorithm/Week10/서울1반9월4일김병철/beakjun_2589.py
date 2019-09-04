def dfs(temp, x, y):
    stack = (x, y)
    while stack:


N, M = map(int, input().split())
island = []
for i in range(N):
    island.append(list(input()))
