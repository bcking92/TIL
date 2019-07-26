test = int(input())
for t in range(test):
    a = int(input())
    da, db, dc, dd, de, df, dg, dh = 0, 0, 0, 0, 0, 0, 0,0
    while a != 0: 
        if a >= 50000:
            a -= 50000
            da += 1
        elif a >= 10000:
            a -= 10000
            db += 1
        elif a >= 5000:
            a -= 5000
            dc += 1
        elif a >= 1000:
            a -= 1000
            dd += 1
        elif a >= 500:
            a -= 500
            de += 1
        elif a >= 100:
            a -= 100
            df += 1
        elif a >= 50:
            a -= 50
            dg += 1
        elif a >=10:
            a -= 10
            dh += 1
        else:
            a = 0
    print('#'+str(t+1))
    print('{0} {1} {2} {3} {4} {5} {6} {7}'.format(da, db, dc, dd, de, df, dg, dh))