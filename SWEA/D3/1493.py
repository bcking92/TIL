import sys

sys.stdin = open('input.txt', 'r')


def cal_1(x):
    if x == 1:
        return [1,1]
    i = 1
    while True:
        if 1+ (i-1)*i//2 <= x < i * (i + 1) // 2 + 1:
            break
        i +=1
    plus = x - (1+ (i-1)*i//2)
    sp = 1, i
    p, q = 1 + plus, i - plus
    result = [p, q]

    return result


def cal_2(p, q):
    n = q + p - 1
    result = int(n * (n - 1) / 2) + p

    return result


for i in range(int(input())):
    p, q = map(int, input().split())
    x, y = cal_1(p)[0] + cal_1(q)[0], cal_1(p)[1] + cal_1(q)[1]
    print('#{} {}'.format(i+1, cal_2(x, y)))
