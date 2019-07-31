for i in range(10):
    a,b,c=int(input()),list(map(int,input().split())),0
    for j in range(2,a-2):
        d=sorted(b[j-2:j+3])[3]
        if b[j]>d:c+=b[j]-d
    print('#%i %i'%(i+1,c))

