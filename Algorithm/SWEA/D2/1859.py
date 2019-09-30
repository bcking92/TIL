import sys

sys.stdin = open('input.txt', 'r')

for i in range(int(input())):
    a = input()
    b = list(map(int,input().split()))
    revenue = 0
    while b:
        temp = max(b)
        peak_index = b.index(temp)
        for j in b[:peak_index]:
            revenue += temp - j
        # revenue += temp*peak_index - sum(b[:peak_index])
        b = b[peak_index+1:]
    print('#%i %i'%(i+1,revenue))