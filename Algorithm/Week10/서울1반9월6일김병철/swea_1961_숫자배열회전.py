for T in range(int(input())):
    N = int(input())
    arr = [list(input().split()) for i in range(N)]
    arr90 = list(zip(*arr[::-1]))
    arr180 = list(zip(*arr90[::-1]))
    arr270 = list(zip(*arr180[::-1]))
    print('#{}'.format(T + 1))
    for i in range(N):
        print(''.join(arr90[i]), ''.join(arr180[i]), ''.join(arr270[i]))
