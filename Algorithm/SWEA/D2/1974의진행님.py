# for i in range(int(input())):
#     ls = [0]*9
#     tt = [0]*3
#     print(ls)
#     print(tt)
#     result = 1
#     for j in range(9):
#         line = list(map(int, input().split()))
#         if sum(line) != 45:
#             result = 0
#         ls = list(map(lambda x : x[0]+x[1] , zip(ls,line)))
#         tt = list(map(lambda x: x[0] + x[1], zip(tt, [sum(line[0:3]), sum(line[3:6]), sum(line[6:9])])))
#         if j % 3 == 2 :
#             if 45 not in tt:
#                 result = 0
#             tt = [0]*3        
#     for sls in ls:
#         if sls != 45:
#             result = 0
#     print('#{0} {1}'.format(i+1, result))

ls = [0,0,0,0,0,0,0,0,0]
line = [1,2,3,4,5,6,7,8,9]
tt = [0,0,0]
print(list(map(lambda x : x[0]+x[1] , zip(ls,line))))
print(list(map(lambda x: x[0] + x[1], zip(tt, [sum(line[0:3]), sum(line[3:6]), sum(line[6:9])]))))