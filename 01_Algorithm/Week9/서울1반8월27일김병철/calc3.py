import sys

sys.stdin = open('input.txt', 'r')
n = '1234567980'
for T in range(10):
    L = int(input())
    calc = []
    trans = ''
    for i in input():
        if i.isdigit():
            trans += i
        else:
            if not calc:
                calc.append(i)
            elif i == '(':
                calc.append(i)
            elif i == '+' or i == '-':
                if calc[-1] == '(':
                    calc.append(i)
                elif calc[-1] == '*' or calc[-1] == '/':
                    while calc[-1] == '*' or calc[-1] == '/':
                        trans += calc.pop()
                    calc.append(i)
                else:
                    calc.append(i)
            elif i == '*' or i == '/':
                calc.append(i)
            elif i == ')':
                while calc[-1] != '(':
                    trans += calc.pop()
                calc.pop()
    stack = []
    for i in trans:
        if i in n:
            stack.append(int(i))
        elif i == '+':
            temp = stack.pop() + stack.pop()
            stack.append(temp)
        elif i == '*':
            temp = stack.pop() * stack.pop()
            stack.append(temp)
    print('#{} {}'.format(T+1, stack[0]))

