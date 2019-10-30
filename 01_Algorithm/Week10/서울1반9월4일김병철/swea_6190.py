for T in range(int(input())):
    N = int(input())
    arr = tuple(reversed(sorted(list(map(int, input().split())))))
    stack = []
    flag = 0
    for i in range(N-1):
        for j in range(i + 1, N):
            stack.append(arr[i] * arr[j])
    stack = tuple(sorted(stack, reverse=True))
    for i in stack:
        temp = str(i)
        for k in range(len(temp) - 1):
            if int(temp[k]) > int(temp[k + 1]):
                break
        else:
            flag = 1
            print('#{} {}'.format(T + 1, temp))
            break
    if not flag:
        print('#{} {}'.format(T + 1, -1))






