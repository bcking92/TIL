dic = {
   's': [1, 2, 3],
   1: [4, 5, 6],
   2: [7, 8, 9],
   3: [10, 11, 12],
}
# 1. 전체

# def dfs(x):
#
#     if dic.get(x):
#         for i in dic[x]:
#             result.append(i)
#             dfs(i)
#             result.pop()
#     else:
#         print(result)
#
# result = [0]
# dfs(0)

# 2. 짝수 안들리기

def dfs(x):
    print(x)
    if type(x) == int:
        if x % 2:
            if dic.get(x):
                for i in dic[x]:
                    result.append(i)
                    dfs(i)
                    result.pop()
            else:
                print(result)
    else:
        if dic.get(x):
            for i in dic[x]:
                result.append(i)
                dfs(i)
                result.pop()
        else:
            print(result)

result = ["s"]
dfs('s')