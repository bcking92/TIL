# import sys
#
# sys.stdin = open('sample_input.txt', 'r')

barcode = {
	'0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

hex_to_bin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}
# barcode2 = {
# 	 0 : '0001101',
#      1 : '0011001',
#      2 : '0010011',
#      3 : '0111101',
#      4 : '0100011',
#      5 : '0110001',
#      6 : '0101111',
#      7 : '0111011',
#      8 : '0110111',
#      9 : '0001011',
# }


for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    bin_arr = ['' for _ in range(N)]
    code = []
    code_bi = []
    code_dec = []
    result = 0
    # print(arr)
    for i in range(N):
        for j in range(M):
            bin_arr[i] += hex_to_bin[arr[i][j]]
    for i in range(N):
        bin_arr[i] = bin_arr[i].strip('0')

    print(set(bin_arr))

    for i in bin_arr:
        if i:
            for j in range(len(i)):
                width = 1
                while True:
                    if barcode.get(i[-1:-8 * width:-1 * width]):
                        break
                    else:
                        width += 1
                code.append()

    # for i in code:
    #     bin_code = str(bin(int('0x' + i, 16))).strip('0b')
    #     v = len(bin_code)//53
    #     code_bi.append('0' * (56 * v - len(bin_code)) + bin_code)
    #
    # for i in code_bi:
    #     len_i = len(i)
    #
    #     decimal = []
    #     for j in range(0, len_i, 7 * (len_i//56)):
    #         imsi = i[j:j + 7 * (len_i//56)]
    #
    #         imsi2 = ''
    #         for k in range(0, len(imsi), (len_i//56)):
    #
    #             imsi2 += imsi[k]
    #         if barcode.get(imsi2) or '0001101' == imsi2:
    #             go = True
    #             decimal.append(int(barcode[imsi2]))
    #         else:
    #             go = False
    #             break
    #     if go:
    #         code_dec.append(decimal)
    # for i in code_dec:
    #     if not ((i[0] + i[2] + i[4] + i[6]) * 3 + i[1] + i[3] + i[5] + i[7]) % 10:
    #         result += sum(i)
    # if not result:
    #     print('#{} {}'.format(T+1, result))
    # else:
    #     print('#{} {}'.format(T+1, result))

# a = '75755027'
# result = ''
# for i in a:
#     temp = barcode2[int(i)]
#     temp2 = ''
#     for j in temp:
#         temp2 += j * 2
#     result += temp2
#
# print(result)
# print(hex(int('0b' + result[2:], 2))[2:])


# print(len('0003f3cf033f3cf033c0c0f30c3cfcf000'))
'''
3 34
0000000000000000000000000000000000
0003f3cf033f3cf033c0c0f30c3cfcf0000003f3cf033f3cf033c0c0f30c3cfcf000
0000000000000000000000000000000000
'''
# print("033c0c0f30c3cfcf00000003f3cf033f3cf033c55500c0f30c3cfcf000".rstrip('0').split('00'))

print()