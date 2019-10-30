a = int(input())
for i in range(a):
    P,Q,R,S,W = tuple(map(int,input().split(' ')))
    A = W * P
    if W < R:
        B = Q
    else:
        B = Q + (W-R) * S
    print('#{0} {1}'.format(i+1,min(A,B)))