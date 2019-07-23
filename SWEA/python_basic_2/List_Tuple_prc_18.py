a = input()
b = a.split(',')
matrix = []
for i in range(int(b[0].strip())):
    column = []
    for j in range(int(b[1].strip())):
        column.append(i*j)
    matrix.append(column)
print(matrix)