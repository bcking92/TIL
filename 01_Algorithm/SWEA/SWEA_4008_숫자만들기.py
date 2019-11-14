import sys, math

sys.stdin = open('sample_input.txt', 'r')

def permutation(arr):
    if sum(visited) == l:
        permu[tuple(temp[:])] = 1
    else:
        for i in range(l):
            if not visited[i]:
                if not dotgo.get(tuple(temp)):
                    visited[i] = 1
                    temp.append(operators[i])
                    permutation(arr)
                    dotgo[tuple(temp[:])] = 1
                    temp.pop()
                    visited[i] = 0

for T in range(int(input())):
    permu = {}
    dotgo = {}
    temp = []
    now_max = -999999999
    now_min = 999999999
    N = int(input())
    operator = tuple(map(int, input().split()))
    operators = []
    for i in range(4):
        if i == 0:
            for j in range(operator[i]):
                operators.append('+')
        elif i == 1:
            for j in range(operator[i]):
                operators.append('-')
        elif i == 2:
            for j in range(operator[i]):
                operators.append('*')
        else:
            for j in range(operator[i]):
                operators.append('/')

    numbers = list(map(int, input().split()))
    l = len(operators)
    visited = [0 for i in range(l)]
    permutation(operators)
    # print(dotgo)
    for case in permu.keys():
        a = 'a'
        b = 'b'
        c = 0
        for i in range(2 * N - 1):
            if i % 2 == 0:
                if a == 'a':
                    a = numbers[i//2]
                else:
                    b = numbers[i//2]
            else:
                c = case[i//2]
            if b != 'b':
                if c == '+':
                    a = a + b
                elif c == '-':
                    a = a - b
                elif c == '*':
                    a = a * b
                elif c == '/':
                    a = int(a/b)
                b = 'b'
        if a > now_max:
            now_max = a
        if a < now_min:
            now_min = a

    print('#{} {}'.format(T+1, now_max - now_min))
print(int(-2/3))
print(-2//3)
print(math.floor(-2/3))
print(math.ceil(-2/3))
print(round(-2/3))
print('-----------------')
print(int(-1/3))
print(-1//3)
print(math.floor(-1/3))
print(math.ceil(-1/3))
print(round(-1/3))
print('-----------------')
print(int(1/3))
print(1//3)
print(math.floor(1/3))
print(math.ceil(1/3))
print(round(1/3))
