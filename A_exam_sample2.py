direction = [(0,1),(0,-1),(-1,0),(1,0)]

for T in range(int(input())):
    N = int(input())
    result = 0
    atoms = {}
    for i in range(N):
        x, y, d, e = map(int, input().split())
        atoms[(2 * x, 2 * y)] = [d, e]

    while True:
        atoms_new = {}
        for location, value in atoms.items():
            if value[0] != 4:
                temp_x = location[0] + direction[value[0]][0]
                temp_y = location[1] + direction[value[0]][1]
                if atoms_new.get((temp_x, temp_y)):
                    atoms_new[(temp_x,temp_y)] = [4, value[1] + atoms_new[(temp_x,temp_y)][1]]
                else:
                    if temp_x in range(-2000, 2000) and temp_y in range(-2000, 2000):
                        atoms_new[(temp_x,temp_y)] = [value[0], value[1]]
        for j in atoms_new.values():
            if j[0] == 4:
                result += j[1]
        atoms = atoms_new
        if not atoms:
            break
        else:
            for j in atoms.values():
                if j[0] != 4:
                    break
            else:
                break
    for i in atoms.values():
        result += i[1]

    print('#{} {}'.format(T + 1, result))


