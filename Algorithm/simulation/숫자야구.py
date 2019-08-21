# 첫 번째 방법..

# hoobo = [1 for i in range(0,1000)]
#
# for i in range(101):
#     hoobo[i] = 0
# for i in range(101,1000):
#     if len(set(str(i))) != 3:
#         hoobo[i] = 0
#     if '0' in str(i):
#         hoobo[i] = 0
#
# for i in range(int(input())):
#     young, strike, ball = map(int,input().split())
#     if strike != 3:
#         hoobo[young] = 0
#         for j in range(101,1000):
#             if len(set(str(young)) & set(str(j))) != strike + ball:
#                 hoobo[j] = 0
#             cnt = 0
#             for k in range(3):
#                 if str(young)[k] == str(j)[k]:
#                     cnt += 1
#             if cnt != strike:
#                 hoobo[j] = 0
#     else:
#         result = 1
#         break
#     result = sum(hoobo)
# print(result)

# 두 번째 방법..


strike = 0
ball = 0
hoobo = []

for i in range(int(input())):
    young, strike, ball = map(int,input().split())
    young = str(young)
    if hoobo:
        for j in hoobo:
            temp_strike = 0
            temp_ball = 0
            for k in range(3):
                if str(j)[k] == young[k]:
                    temp_strike += 1
                else:
                    if str(j)[k] in young:
                        temp_ball += 1
            if strike != temp_strike or ball != temp_ball or '0' in str(j):
                hoobo.remove(j)
    else:

        for j in range(101,988):
            temp_strike = 0
            temp_ball = 0
            for k in range(3):
                if str(j)[k] == young[k]:
                    temp_strike += 1
                else:
                    if str(j)[k] in young:
                        temp_ball += 1
            if strike == temp_strike and ball == temp_ball:
                hoobo.append(j)
print(len(hoobo))





