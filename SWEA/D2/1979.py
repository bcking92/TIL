a = int(input())
for i in range(a):
    b = input().split()
    N, K = int(b[0]),int(b[1])
    matrix = []
    K_list = []

    for j in range(N):
        matrix.append(list(map(int,input().split())))
    
    matrix_90 = list(zip(*matrix[::-1]))
    matrix_180 = list(zip(*matrix_90[::-1]))
    matrix_270 = list(map(list,list(zip(*matrix_180[::-1]))))

    for j in range(N):
        suc = 0
        for k in range(N):
            if matrix[j][k] == 1:
                suc += 1
            else:
                K_list.append(suc)
                suc = 0 
        K_list.append(suc)
    for j in range(N):
        suc = 0
        for k in range(N):
            if matrix_270[j][k] == 1:
                suc += 1
            else:
                K_list.append(suc)
                suc = 0
        K_list.append(suc)

    print('#{} {}'.format(i+1,K_list.count(K)))
       
