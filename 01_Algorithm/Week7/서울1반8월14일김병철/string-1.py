''' incoding UTF-8 '''
# 1. String 뒤집기 revese() slicing을 쓰지 않고 만들어보기.

# s = 'Reverse this strings'
# temp = ''
# for i in s:
#     temp = i + temp
# print(temp)

# 2. i to a 구현해보기.
str = "0123456789"
s = 165198019819889749512163
temp = ''
while True:
    temp = chr((s % 10)+ 48) + temp
    s //= 10
    if s == 0:
        break
print(temp)