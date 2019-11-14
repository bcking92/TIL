import sys

sys.stdin = open('sample_input.txt', 'r')

def find_peek():
    peek = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > peek:
                peek = mountain[i][j]
    return peek

def find_longest_path(x, y, l, visited):
    global longest_path
    if l > longest_path:
        longest_path = l
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        temp_x = x + dx
        temp_y = y + dy
        if 0 <= temp_x < N and 0 <= temp_y < N:
            if mountain[temp_x][temp_y] < mountain[x][y]:
                if (temp_x, temp_y) not in visited:
                    find_longest_path(temp_x, temp_y, l+1, visited + [(temp_x, temp_y)])

for T in range(int(input())):
    longest_path = 0
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
                    if mountain[i][j] - k >= 0:
                        mountain[i][j] -= k
                        find_longest_path(*peek, 1, [peek])
                        mountain[i][j] += k
    print('#{} {}'.format(T+1, longest_path))
    