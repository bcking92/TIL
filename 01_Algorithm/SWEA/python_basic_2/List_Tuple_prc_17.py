import math

a = input()
b = a.split(', ')
b = [round(int(x)*2*math.pi,2) for x in b ]
print(str(b)[1:-1])