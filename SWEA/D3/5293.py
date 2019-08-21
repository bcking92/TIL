
def johap(x):


for T in range(int(input())):
    ejin = []
    result = ''
    A, B, C, D = map(int,input().split())
    for i in [('00', A), ('01',B), ('10',C), ('11',D)]:
        for j in range(i[1]):
            ejin.append(i[0])
