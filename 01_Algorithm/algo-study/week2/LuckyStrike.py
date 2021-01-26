'''
# 백준 18406번
합(앞) == 합(뒤) 이면 LUCKY 아니면 READY
'''


def solution(score):
    n = len(score)
    num_input = tuple(map(int, score))
    if sum(num_input[:n//2]) == sum(num_input[n//2:]):
        return 'LUCKY'
    else:
        return 'READY'


score = input()
print(solution(score))

