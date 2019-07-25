import collections

a = int(input())
b = []
c = []
for i in range(a):
    b.append(input())

for j in range(len(b)):
    if j % 2 == 1:
        c.append(b[j])

for k in range(len(c)):
    d = max(c[k], key = lambda x: c[k].count(x))
    e = {x for x in c[k] if c[k].count(x) == c[k].count(d)}
    print('#{0} {1}'.format(k+1,max(e)))
    


   
# # print(max({'dd':2, 'df':3, 'aa':6}.values()))
# # (dd,2).sort(lambda x: x[1])
# a = [1,2,3,1,2,1,2]
# # b = max(a.items(), key=lambda kv: kv[1])
# b = max(a, key=lambda x: a.count(x))
# c = {x for x in a if a.count(x) == a.count(b)}
# print(b)
# print(a.count(b))
# print(c)