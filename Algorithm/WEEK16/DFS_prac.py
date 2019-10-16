def dfs(x):
    global nei_list, visited
    stack = [x]
    visited[x] = 1
    print(x, end=' ')
    while stack:
        temp = stack.pop()
        if not visited[temp]:
            print(temp, end=' ')
            visited[temp] = 1
        if nei_list[temp]:
            for i in nei_list[temp]:
                if not visited[i]:
                    stack.append(i)
def bfs(x):
    global nei_list, visited
    queue = [x]
    visited[x] = 1
    while queue:
        temp = queue.pop(0)
        print(temp, end=' ')
        if nei_list[temp]:
            for i in nei_list[temp]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)

arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

nei_list = [[] for i in range(max(arr)+1)]
visited = [0 for i in range(max(arr)+1)]
for i in range(0, len(arr), 2):
    nei_list[arr[i]].append(arr[i+1])
    nei_list[arr[i+1]].append(arr[i])
print('nei_list')
print(nei_list)
print('----dfs----')
dfs(1)
visited = [0 for i in range(max(arr)+1)]
print()
print('-----bfs-----')
bfs(1)