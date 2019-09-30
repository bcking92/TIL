a = input()
b = a.replace(' ','').split(',')
c = sorted(b)
print(str(c).strip('[').strip(']').replace('\'',''))
