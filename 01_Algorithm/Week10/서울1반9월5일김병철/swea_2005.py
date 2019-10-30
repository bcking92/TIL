for T in range(int(input())):
    num = int(input())
    print('#{}'.format(T+1))
    for i in range(num):
        if i == 0:
            a = i + 1
            print(i+1)
        else:
            a = a * 10 + a
            for j in str(a):
                print(j, end= ' ')
            print()