# with open('ssafy.txt', 'w', encoding = "utf-8") as f :
#     for i in range(5) :
#         f.write("with with 사용\n")

with open('ssafy.txt', 'r', encoding = "utf-8") as f :
    result = f.read()


print(type(result))
