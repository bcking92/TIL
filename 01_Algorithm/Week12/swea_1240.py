def search():
    global a, b
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                a, b = i, j
                return

barcode = {
	'0001101' : '0',
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    a, b, temp = 0, 0, ''
    search()
    num = []
    c = arr[a]
    for i in range(1, 57, 7):
        num.append(int(barcode[c[b - 56 + i: b - 56 + i + 7]]))
    if not ((num[0] + num[2] + num[4] + num[6]) * 3 + num[1] + num[3] + num[5] + num[7]) % 10:
        print('#%i %i'% (T+1, sum(num)))
    else:
        print('#%i %i'% (T+1, 0))