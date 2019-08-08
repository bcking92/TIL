for i in range(int(input())):
    N, a = int(input()), list(map(int, input().split()))
    result = ''
    for j in range(10):
        max_now = 0
        min_now = 101
        for k in range(N):
            if j % 2:
                if a[k] < min_now:
                    min_now = a[k]
                    min_index = k
            else:
                if a[k] > max_now and a[k] <= 100:
                    max_now = a[k]
                    max_index = k
        if j % 2:
            result += str(min_now) + ' '
            a[min_index] = 101
        else:
            result += str(max_now) + ' '
            a[max_index] = 101

    print('#{} {}'.format(i + 1, result))