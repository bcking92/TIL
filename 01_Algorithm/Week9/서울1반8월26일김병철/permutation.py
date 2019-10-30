
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

subset = []

memoization = [0 for i in range(11)]


visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def dfs(arr, x, k):
    if x == k:
        temp = []
        for i in range(10):
            if memoization[i+1]:
                temp.append(memoization[i+1])
        subset.append(temp)
    else:
        x += 1
        for i in range(10):
            if not visited[i]:
                memoization[x] = num_list[i]
                visited[i] = 1
                dfs(arr, x, k)
                visited[i] = 0

dfs(num_list, 0, 3)
print(subset)
