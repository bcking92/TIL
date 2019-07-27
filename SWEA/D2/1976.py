for i in range(int(input())):
    t = list(map(int,input().split()))
    minp = 0 if t[1] + t[3] < 60 else 1
    mins = t[1] + t[3] if t[1] + t[3] < 60 else t[1] + t[3] - 60
    hours = t[0]+ t[2] + minp if t[0] + t[2] + minp <= 12 else t[0] + t[2] + minp - 12
    print('#{0} {1} {2}'.format(i+1,hours,mins))