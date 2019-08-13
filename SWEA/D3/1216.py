import sys

sys.stdin = open('input.txt', 'r')

def hoe_moon(x):
    result = ''
    for i in range(100):
        for j in range(i):
            result = x[0+j:100-i+j]
            if result == result[::-1]:
                return result
    return ''

for i in range(10):
    input()
    matrix = []
    max_len = 0
    for j in range(100):
        matrix.append(input())
    matrix_y = list(map(lambda x: ''.join(x),list(zip(*matrix))))
    for j in matrix:
        if len(hoe_moon(j)) > max_len :
            max_len = len(hoe_moon(j))
    for j in matrix_y:
        if len(hoe_moon(j)) > max_len :
            max_len = len(hoe_moon(j))            
    print('#{} {}'.format(i+1,max_len))