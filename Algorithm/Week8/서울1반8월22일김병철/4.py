for T in range(int(input())):
    str1 = input()
    a = len(str1)
    result = list(str1)
    while True:
        for i in range(len(result)-1):
            if result[i] == result[i+1]:
                result.pop(i)
                result.pop(i)
                break
        else:
            break
    print('#{} {}'.format(T+1, len(result)))