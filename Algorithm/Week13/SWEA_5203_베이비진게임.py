import sys

sys.stdin = open('input.txt', 'r')

for T in range(int(input())):
    cards = tuple(map(int, input().split()))
    A, B = [], []
    end = 0
    A_cnt = [0] * 10
    B_cnt = [0] * 10
    for i in range(0, 12, 2):
        A_cnt[cards[i]] += 1
        if max(A_cnt) >= 3:
            print('#{} {}'.format(T + 1, 1))
            break
        for j in range(2, 10):
            if A_cnt[j] and A_cnt[j-1] and A_cnt[j-2]:
                print('#{} {}'.format(T + 1, 1))
                end = 1
                break
        if end:
            break
        B_cnt[cards[i+1]] += 1
        if max(B_cnt) >= 3:
            print('#{} {}'.format(T + 1, 2))
            break
        for j in range(2, 10):
            if B_cnt[j] and B_cnt[j-1] and B_cnt[j-2]:
                print('#{} {}'.format(T + 1, 2))
                end = 1
                break
        if end:
            break

    else:
        print('#{} {}'.format(T + 1, 0))




