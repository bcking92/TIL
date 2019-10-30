for T in range(int(input())):
    binary, ternary = input(), input()
    result = 0
    candi_1 = []
    candi_2 = []
    for i in range(len(binary)):
        if binary[i] == '1':
            temp = binary[:i] + '0' + binary[i+1:]
            temp_dec_1 = 0
            for j in range(len(temp)):
                temp_dec_1 += int(temp[len(temp) - 1 - j]) * (2 ** j)
            candi_1.append(temp_dec_1)
        else:
            temp = binary[:i] + '1' + binary[i+1:]
            temp_dec_1 = 0
            for j in range(len(temp)):
                temp_dec_1 += int(temp[len(temp) - 1 - j]) * (2 ** j)
            candi_1.append(temp_dec_1)
    for i in range(len(ternary)):
        if ternary[i] == '2':
            temp1 = ternary[:i] + '1' + ternary[i+1:]
            temp2 = ternary[:i] + '0' + ternary[i+1:]
            temp_dec_1 = 0
            temp_dec_2 = 0

            for j in range(len(temp1)):
                temp_dec_1 += int(temp1[len(temp1) - 1 - j]) * (3 ** j)
                temp_dec_2 += int(temp2[len(temp2) - 1 - j]) * (3 ** j)
            candi_2.append(temp_dec_1)
            candi_2.append(temp_dec_2)
        elif ternary[i] == '1':
            temp1 = ternary[:i] + '2' + ternary[i+1:]
            temp2 = ternary[:i] + '0' + ternary[i+1:]
            temp_dec_1 = 0
            temp_dec_2 = 0

            for j in range(len(temp1)):
                temp_dec_1 += int(temp1[len(temp1) - 1 - j]) * (3 ** j)
                temp_dec_2 += int(temp2[len(temp2) - 1 - j]) * (3 ** j)
            candi_2.append(temp_dec_1)
            candi_2.append(temp_dec_2)
        else:
            temp1 = ternary[:i] + '1' + ternary[i+1:]
            temp2 = ternary[:i] + '2' + ternary[i+1:]
            temp_dec_1 = 0
            temp_dec_2 = 0

            for j in range(len(temp1)):
                temp_dec_1 += int(temp1[len(temp1) - 1 - j]) * (3 ** j)
                temp_dec_2 += int(temp2[len(temp2) - 1 - j]) * (3 ** j)
            candi_2.append(temp_dec_1)
            candi_2.append(temp_dec_2)
    # print(candi_1)
    # print(candi_2)
    for i in candi_1:
        for j in candi_2:
            if i == j:
                result = i
                break
        if result:
            break
    print('#{} {}'.format(T + 1, result))