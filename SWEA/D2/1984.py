a = int(input())

for i in range(a):
    b = list(map(int,input().split()))
    b.remove(max(b))
    b.remove(min(b))
    d = round(sum(b)/8)
    print('#{} {}'.format(i+1,d))



# a = int(input())
# for i in range(a):
#     b = sorted(list(map(int,input().split())))
#     c = round(sum(b[1:-1])/8)
#     print('#{} {}'.format(i+1,c))
