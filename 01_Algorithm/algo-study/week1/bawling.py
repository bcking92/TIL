def solution(N, M, balls):
    ball_list = list(map(int, balls.split(' ')))
    result = 0
    for i in range(N):
        for j in range(i, N):
            if ball_list[i] != ball_list[j]:
                result += 1
    return result

print(solution(5, 3, '1 3 2 3 2'))
print(solution(8, 5, '1 5 4 3 2 4 5 2'))