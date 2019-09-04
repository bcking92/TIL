for T in range(int(input())):
    arr, mx, result = [tuple(input()) for i in range(5)], 0, ''
    # arr = tuple(zip(*arr))
    for i in arr:
        if len(i) > mx: mx = len(i)
    for i in range(mx):
        for j in range(5):
            if i < len(arr[j]):result += arr[j][i]
    print('#{} {}'.format(T+1, result))
    # print(arr)