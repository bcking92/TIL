import sys

sys.stdin = open('sample_input.txt', 'r')

def combination(arr):
    combi = []
    for i in range(1 << (len(arr) -1)):
        a = []
        b = []
        if len(bin(i & (2 ** len(arr) - 1)).strip('0b').replace('0', '')) == N//2:
            for j in range(len(arr)):
                if i & (1 << j):
                    a.append(arr[j])
                else:
                    b.append(arr[j])
            combi.append((a, b))
    return combi

for T in range(int(input())):
    result = 10000000
    N = int(input())
    food = [i for i in range(N)]
    arr = [tuple(map(int, input().split())) for i in range(N)]
    combi = combination(food)
    for sub in combi:
        taste_A = 0
        for i in sub[0]:
            for j in sub[0]:
                taste_A += arr[i][j]
        taste_B = 0
        for i in sub[1]:
            for j in sub[1]:
                taste_B += arr[i][j]
        temp = abs(taste_A - taste_B)
        if result > temp:
            result = temp

    print('#{} {}'.format(T+1, result))