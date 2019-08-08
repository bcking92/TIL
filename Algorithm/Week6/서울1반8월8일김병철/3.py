def try_num(x,P):
    first = 1
    last = P
    try_n = 0
    while True:
        try_n += 1
        search = int((first+last)/2)
        if  search == x:
            break
        else:
            if search > x:
                last = search
            else:
                first = search
    return try_n

for i in range(int(input())):
    P, A, B = map(int,input().split())
    if try_num(A,P) > try_num(B,P):
        print('#{} {}'.format(i+1,'B'))
    elif try_num(A,P) < try_num(B,P):
        print('#{} {}'.format(i+1,'A'))
    else:
        print('#{} {}'.format(i+1,0))