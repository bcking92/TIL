a = int(input())
b = a.split(', ')
matrix = []
for i in int(b[1]):
    column = []
    for j in int(b[0]):
        column.append(i*j)
    matrix.append(column)
print(matrix)