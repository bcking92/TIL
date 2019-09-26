def down(arr):
    if len(arr) == 1:
        return arr[0]
    middle = N//2
    l = arr[:middle]
    r = arr[middle:]

    l = down(l)
    r = down(r)
    return up(l, r)

def up(left, right):
    result = []
    while True:
        for i in left:
            for j in right:
                if j <= i:
                    result.append(j)
                else:
                    result.append(i)
                    break

            for
        else:



for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge(arr)