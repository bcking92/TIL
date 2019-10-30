for T in range(int(input())):
    N = int(input())
    AB = [tuple(map(int, input().split())) for i in range(N)]
    P = int(input())
    C = [int(input())for i in range(P)]
    result = [0] * 5001
    for i in AB:
        for j in range(i[0], i[1] + 1):
            result[j] += 1
    result2 = []
    for i in C:
        result2.append(result[i])
    print('#{} {}'.format(T+1, ' '.join(map(str, result2))))

