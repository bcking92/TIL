def dfs(x):
    global visited
    # if link.get(x):
    #     for i in link[x]:
    #         if not visited.get(i):
    #             visited[i] = 1
    #             dfs(i)
    #             visited[i] = 0

    stack = [x]
    while stack:
        t = stack.pop()
        if link.get(t):
            for i in link[t]:
                if not visited.get(i):
                    visited[i] = 1
                    stack.append(i)
N = int(input())
L = int(input())
link = {}
visited = {'1' : 1}
result = 0
for i in range(L):
    a, b = input().split()
    if not link.get(a):
        link[a] = [b]
    else:
        link[a].append(b)
    if not link.get(b):
        link[b] = [a]
    else:
        link[b].append(a)
dfs('1')
print(len(visited) - 1)
