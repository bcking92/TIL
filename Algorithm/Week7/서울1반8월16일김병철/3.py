for i in range(int(input())):
    str1, str2 = input(), input()
    result = 0
    for j in str1:
        cnt = 0
        for k in str2:
            if j == k:
                cnt += 1
        if result < cnt:
            result = cnt
    print('#{} {}'.format(i + 1, result))