import sys

sys.stdin = open('sample_input.txt', 'r')

for T in range(int(input())):
    N, M, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for i in range(N)]
    cells = {}
    died = {}
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cells[(i, j)] = [arr[i][j], arr[i][j] - 1, 'deactivated']
    for k in range(K):
        # print(cells.keys())
        new_cells = {}
        for key, value in cells.items():
            if value[2] == 'died':
                died[key] = 1
            elif value[2] == 'deactivated':
                if value[1] == 0:
                    new_cells[key] = [value[0], value[0] - 1, 'activated']
                else:
                    new_cells[key] = [value[0], value[1] - 1, 'deactivated']
            elif value[2] == 'activated':
                if value[1] == 0:
                    new_cells[key] = [value[0], value[1], 'died']
                else:
                    new_cells[key] = [value[0], value[1] - 1, 'activated']
                if value[0] - value[1] == 1:
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        if not died.get((key[0] + dx, key[1] + dy)) and not cells.get((key[0] + dx, key[1] + dy)):
                            if new_cells.get((key[0] + dx, key[1] + dy)):
                                if not cells.get((key[0] + dx, key[1] + dy)):
                                    if new_cells[(key[0] + dx, key[1] + dy)][0] < value[0]:
                                        new_cells[(key[0] + dx, key[1] + dy)] = [value[0], value[0] - 1, 'deactivated']
                            else:
                                new_cells[(key[0] + dx, key[1] + dy)] = [value[0], value[0] - 1, 'deactivated']
        cells = new_cells  
    for k, v in cells.items():
        if v[2] != 'died':
            result += 1
    print('#{} {}'.format(T+1, result))