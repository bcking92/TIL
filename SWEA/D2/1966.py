j=int(input())
for t in range(j):
    n,l=input(),list(map(int,input().split(' ')))
    print('#'+str(t+1)+' '+str(sorted(l))[1:-1].replace(',',''))