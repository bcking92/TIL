import sys

sys.stdin = open('input.txt', 'r')

def connect_nasa(nasas):
    max_len = []
    result = ''
    for i in range(0,len(nasas),2):
        used_nasa = []
        now_nasa = [nasas[i], nasas[i + 1]]
        used_nasa.append(i)
        while True:
            for j in range(0,len(nasas), 2):
                if j not in used_nasa:
                    if nasas[j] == now_nasa[-1]:
                        now_nasa.append(nasas[j])
                        now_nasa.append(nasas[j+1])
                        used_nasa.append(j)
                        break
            else:
                break
        if len(max_len) < len(now_nasa):
            max_len = now_nasa
    for i in max_len:
        result += str(i)+' '
    return result

for i in range(int(input())):
    N, nasas = int(input()), list(map(int, input().split()))
    print('#{} {}'.format(i+1,connect_nasa(nasas)))