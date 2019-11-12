import sys

sys.stdin = open('sample_input.txt', 'r')

def find_peek():
    peek = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > peek:
                peek = mountain[i][j]
    return peek

def find_longest_path(x, y):
    longest_path = 0
    visited = {}
    x, y = x, y
    stack = [(x, y, 1, [])]
    while stack:
        x, y, d, p = stack.pop()
        p.append((x, y))
        if d > longest_path:
            longest_path = d
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp_x = x + dx
            temp_y = y + dy
            if 0 <= temp_x < N and 0 <= temp_y < N:
                if mountain[temp_x][temp_y] < mountain[x][y]:
                    if (temp_x, temp_y) not in p:
                        stack.append((temp_x, temp_y, d+1, p))

    return longest_path

for T in range(int(input())):
    result = 0
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for i in range(N)]
    top = find_peek()
    peeks = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:
                peeks.append((i, j))
    
    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                for peek in peeks:
                    mountain[i][j] -= k
                    path = find_longest_path(*peek)
                    mountain[i][j] += k
                    if path > result:
                        result = path
    print(result)
    