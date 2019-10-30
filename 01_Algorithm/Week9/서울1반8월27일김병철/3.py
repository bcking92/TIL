import sys

sys.stdin = open('input.txt', 'r')

def rsp(arr, x, y):
    if arr[x] == '1' and arr[y] == '2':
        return y
    elif arr[x] == '1' and arr[y] == '3':
        return x
    elif arr[x] == '2' and arr[y] == '1':
        return x
    elif arr[x] == '2' and arr[y] == '3':
        return y
    elif arr[x] == '3' and arr[y] == '1':
        return y
    elif arr[x] == '3' and arr[y] == '2':
        return x
    else:
        return min(x,y)

def card(arr, start, end):
    if start == end:
        return start
    elif end - start == 1:
        return rsp(arr, start, end)
    else:
        middle = (start+end)//2
        left = card(arr, start, middle)
        right = card(arr, middle+1, end)
        return rsp(arr, left, right)

for T in range(int(input())):
    N = int(input())
    arr = input().split()
    print('#{} {}'.format(T+1,card(arr, 0, len(arr)-1)+1))


