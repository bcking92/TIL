a = [x for x in range(1,21) ]
b = [x ** 2 for x in a if x % 3 != 0 or x % 5 !=0 ]
print(b)