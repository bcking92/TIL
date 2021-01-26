def solution(N, coins):
    coin_list = sorted(list(map(int, coins.split(' '))), reverse=True)
    for i in range(1, sum(coin_list)+ 1):
        temp = i
        for j in coin_list:
            if temp < j:
                continue
            else:
                temp -= j
                if temp == 0:
                    break
        else:
            return i
    
print(solution(5, '3 2 1 1 9'))