samyuk = '369'

for i in range(1,int(input())+1):
    clap = ''
    for j in str(i):
        if j in samyuk:
            clap += '-'
    if not clap:
        print(i, end = ' ')
    else:
        print(clap, end = ' ')