import sys

sys.stdin = open('input.txt', 'r')

for T in range(10):
    input()
    result = 0
    matrix = [input().split() for i in range(100)]
    for i in range(100):
        stack = []
        cnt = 0
        for j in range(100):
            if matrix[99 - j][i] != '0':
                stack.append(matrix[99 - j][i])
        while True:
            if stack[-1] == '2':
                stack.pop()
            elif stack[0] == '1':
                stack.pop(0)
            else:
                break
        for j in range(len(stack) - 1):
            if stack[j] != stack[j+1]:
                cnt += 1
        result += (cnt+1)//2
    print('#{} {}'.format(T+1, result))