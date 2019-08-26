num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



subset = []

def make_candidates(arr, x, k, c):
    pass

def dfs(arr, x, k):

    memoization = [0 for i in range(10)]

    if x == k:

        temp = []
        for i in range(10):
            if memoization[i] == 1:
                temp.append(num_list[i])
        if sum(temp) == 10:
            subset.append(temp)
    else:
        x += 1
        memoization[x] = 1



