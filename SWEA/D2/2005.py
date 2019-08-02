for i in range(int(input())):
    num = int(input())
    pascal = 0
    print(f'#{i+1}')
    for j in range(1,num+1):
        if j == 1:
            pascal += j
            print(pascal)
        else:
            pascal += int(str(pascal)+'0')
            for chr in str(pascal):
                print(chr,end=' ')
            print()