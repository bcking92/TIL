import sys

sys.stdin = open('input.txt', 'r')

def dfs(arr, x, N, cur_sum):
    global now_min
    if 자르는 조건:
        return None

    if x == N:
        if now_min > sum(memoization):
            now_min = sum(memoization)
    else:
        if now_min > sum(memoization):
            x += 1
            for i in range(N):
                if not visited[i]:
                    memoization[x-1] = arr[x-1][i]
                    visited[i] = 1
                    dfs(arr, x, N, cur_sum+arr[x-1][i])
                    memoization[x-1] = 0
                    visited[i] = 0

for T in range(int(input())):
    N = int(input())
    matrix = []
    now_min = 1000
    visited = [0 for i in range(N)]
    memoization = [0 for i in range(N)]
    for i in range(N):
        matrix.append(list(map(int,input().split())))
    dfs(matrix, 0, N, 0)
    print('#{} {}'.format(T+1, now_min))