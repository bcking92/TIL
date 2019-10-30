ziphap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(int(input())):
    result = 0
    N, K = map(int,input().split())
    for j in range(1<<12):
        subset_len = 0
        subset_sum = 0
        for k in range(12):
            if j & (1<<k):
                subset_len += 1
                subset_sum += ziphap[k]
        if subset_len == N and subset_sum == K:
            result += 1
    print('#{} {}'.format(i+1,result))