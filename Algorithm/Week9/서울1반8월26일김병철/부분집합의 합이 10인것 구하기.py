num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

subset = []

memoization = [0 for i in range(11)]

def dfs(arr, x, k):
    if x == k:
        temp = []
        for i in range(10):
            if memoization[i+1] == 1:
                temp.append(num_list[i])
        # if sum(temp) == 10:
        subset.append(temp)
    else:
        x += 1
        memoization[x] = 1
        dfs(arr, x, k)
        memoization[x] = 0
        dfs(arr, x, k)

dfs(num_list, 0, 10)
print(subset)


