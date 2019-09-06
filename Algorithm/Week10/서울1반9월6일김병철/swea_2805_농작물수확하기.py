for T in range(int(input())):
    N, result = int(input()), 0
    farm = tuple([tuple(map(int, input())) for i in range(N)])
    for i in range(N//2):
        result += sum(farm[i][N//2 - i: N//2 + 1 + i])
        result += sum(farm[N - 1 - i][N//2 - i: N//2 + 1 + i])
    result += sum(farm[N//2])
    print('#{} {}'.format(T + 1, result))