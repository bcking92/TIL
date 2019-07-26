from datetime import datetime, timedelta, date
a = int(input())
for i in range(a):
    b = list(map(int,input().split(' ')))
    print('#{0} {1}'.format(i+1,int(str(date(2019,b[2],b[3])-date(2019,b[0],b[1])).split(' ')[0])+1))