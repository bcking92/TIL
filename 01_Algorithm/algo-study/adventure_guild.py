def solution(N, players):
    players_list = list(map(int,players.split(' ')))
    num_list = [0 for i in range(N+1)]
    result = 0
    remain = 0
    for i in range(N):
        num_list[players_list[i]] += 1
    for i in range(1, N+1):
        result += num_list[i] // (i)
        now_remain = num_list[i] % (i)
        if (now_remain + remain) // (i) > 0:
            result += (now_remain + remain) // (i)
            remain = (now_remain + remain) % (i)
    return result

print(solution(5, '2 3 1 2 2'))