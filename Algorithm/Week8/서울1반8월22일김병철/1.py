def box(x):
    if x == 1:
        return 1
    elif  x == 2:
        return 3
    return box(x-1) + 2*box(x-2)

for T in range(int(input())):
    print('#{} {}'.format(T+1, box(int(input())//10)))