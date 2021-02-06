'''
# 기둥과 보 설치

문제에서 하라는대로 구현
보가 기둥"위"에 붙어야하는데 기둥아래에도 붙어도 되는줄 알아서 헷갈림
'''


def bo_check(field, x, y):
    if field[x][y][1] == 1 or field[x+1][y][1] == 1 : # 기둥과 연결되어있거나
        return True
    elif field[x][y][3] == 1 and field[x+1][y][2] == 1: # 양옆이 보이거나
        return True
    return False

def pillar_check(field, x, y):
    if y == 0:                # 바닥위거나
        return True
    elif field[x][y][1] == 1: # 기둥위거나
        return True
    elif field[x][y][2] == 1 or field[x][y][3] == 1: # 보위거나
        return True
    return False

def solution(n, build_frame):
    field = [[[0,0,0,0] for i in range(n+1)] for i in range(n+1)] # down, up, left, right
    answer = []

    for x,y,a,b in build_frame:
        if a == 0: # 기둥이면
            if b == 0: # 삭제이면
                field[x][y][0] = 0
                field[x][y+1][1] = 0
                if field[x][y][3] == 1: # 왼쪽아래 보 확인
                    if not bo_check(field, x-1, y):
                        field[x][y][0] = 1
                        field[x][y+1][1] = 1
                        continue
                if field[x][y+1][3] == 1: # 왼쪽위 보 확인
                    if not bo_check(field, x-1, y+1):
                        field[x][y][0] = 1
                        field[x][y+1][1] = 1
                        continue
                if field[x][y][2] == 1: # 오른쪽 아래 보 확인
                    if not bo_check(field, x, y):
                        field[x][y][0] = 1
                        field[x][y+1][1] = 1
                        continue
                if field[x][y+1][2] == 1: # 오른쪽 위 보 확인
                    if not bo_check(field, x, y+1):
                        field[x][y][0] = 1
                        field[x][y+1][1] = 1
                        continue
                if field[x][y+1][0] == 1: # 위 기둥 확인
                    if not pillar_check(field, x, y+1):
                        field[x][y][0] = 1
                        field[x][y+1][1] = 1
                        continue
            else:      # 설치이면
                if field[x][y][0] == 0:
                    if pillar_check(field, x, y):
                        field[x][y][0] = 1
                        field[x][y+1][1] = 1
        else:      # 보이면
            if b == 0: # 삭제이면
                field[x][y][2] = 0
                field[x+1][y][3] = 0
                if field[x][y][0] == 1: # 왼쪽 위 기둥 확인
                    if not pillar_check(field, x, y):
                        field[x][y][2] = 1
                        field[x+1][y][3] = 1
                        continue
                if field[x+1][y][0] == 1: # 오른쪽 위 기둥 확인
                    if not pillar_check(field, x+1, y):
                        field[x][y][2] = 1
                        field[x+1][y][3] = 1
                        continue
                if field[x][y][3] == 1: # 왼쪽 보 확인
                    if not bo_check(field, x-1, y):
                        field[x][y][2] = 1
                        field[x+1][y][3] = 1
                        continue
                if field[x+1][y][2] == 1: # 오른쪽 보 확인
                    if not bo_check(field, x+1, y):
                        field[x][y][2] = 1
                        field[x+1][y][3] = 1
                        continue
            else:      # 설치이면
                if field[x][y][2] == 0:
                    if bo_check(field, x, y):
                        field[x][y][2] = 1
                        field[x+1][y][3] = 1

    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j][0] == 1:
                answer.append([i,j,0])
            if field[i][j][2] == 1:
                answer.append([i,j,1])
                
    return answer

print(solution(5,[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print()
print(solution(5,[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))