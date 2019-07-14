
f = [1,1]
for i in range(2,10):
    f.append(f[i-1]+f[i-2])
print(f)
