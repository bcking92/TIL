import sys

sys.stdin = open('input.txt', 'r')

for T in range(int(input())):
    stack = []
    calc = input().split()
    for i in calc:
        if i == '+':
            if len(stack) > 1:
                temp = stack.pop() + stack.pop()
                stack.append(temp)
            else:
                print('#{} {}'.format(T+1, 'error'))
                break
        elif i == '-':
            if len(stack) > 1:
                temp = -(stack.pop() - stack.pop())
                stack.append(temp)
            else:
                print('#{} {}'.format(T+1, 'error'))
                break
        elif i == '*':
            if len(stack) > 1:
                temp = stack.pop() * stack.pop()
                stack.append(temp)
            else:
                print('#{} {}'.format(T+1, 'error'))
                break
        elif i == '/':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                temp = b // a
                stack.append(temp)
            else:
                print('#{} {}'.format(T+1, 'error'))
                break
        elif i == '.':

            continue

        else:
            if i.isdigit():
                stack.append(int(i))
            else:
                print('#{} {}'.format(T+1, 'error'))
                break
    else:
        if len(stack) == 1:
            print('#{} {}'.format(T+1, stack[0]))
        else:
            print('#{} {}'.format(T + 1, 'error'))