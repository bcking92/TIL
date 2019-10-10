def inorder_search(x, arr):
    x = int(x)
    if arr[x]:
        if len(arr[x]) == 1:
            print(arr[x][0], end='')
        elif len(arr[x]) == 2:
            inorder_search(arr[x][1], arr)
            print(arr[x][0], end='')
        elif len(arr[x]) == 3:
            inorder_search(arr[x][1], arr)
            print(arr[x][0], end='')
            inorder_search(arr[x][2], arr)

for T in range(10):
    arr = [0 for i in range(int(input()) + 1)]
    for i in range(1, len(arr)):
        b = input().split()
        arr[i] = b[1:]
    print('#{} '.format(T+1), end=' ')
    inorder_search(1, arr)
    print()