def ok(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if abs(arr[i] - arr[j]) == abs(i - j):
                        return False
        else:
            return True
    else:
        return True

def dfs(arr, end):
    global N
    global result
    global temp
    global position

    if len(temp) == end:
        if ok(temp):
        	result += 1
    if ok(temp):
        for i in arr:
            if not visited[i]:
                visited[i] = 1
                temp.append(i)
                dfs(arr, end)
                temp.pop()
                visited[i] = 0

for T in range(int(input())):
    N = int(input())
    position = [i for i in range(N)]
    visited = [ 0 for i in range(N)]
    temp = []
    result = 0
    dfs(position, N)
    print('#{} {}'.format(T + 1, result))