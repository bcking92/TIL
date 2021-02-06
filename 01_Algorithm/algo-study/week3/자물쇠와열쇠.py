'''
# 자물쇠와 열쇠

1. 돌리고
2. 모든 경우의수 비교
3. 다시 돌리고
'''

def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    go = True
    temp_lock = [a[:] for a in lock]
    for i in range(4):
        key = list(zip(*key[::-1]))
        print(i)
        for dx in range(M+N): # 가로
            for dy in range(M+N): # 세로
                for x in range(M):
                    for y in range(M):
                        if M-1<= x + dx < M+N-1 and M-1 <= y + dy < M+N-1:
                            temp_lock[x+dx-M+1][y+dy-M+1] += key[x][y]
                for k in range(N):
                    for l in range(N):
                        if temp_lock[k][l] != 1:
                            temp_lock = [a[:] for a in lock]
                            go = False
                            break
                    if not go:
                        go = True
                        break
                else:
                    return True
    return answer