#보이어-무어 알고리즘을 이용했습니다.

for i in range(int(input())):
    str1 = input()
    str2 = input()
    lenstr1 = len(str1) - 1
    jump = 0

    while True:
        if str1[lenstr1] == str2[lenstr1 + jump]:
            for j in range(lenstr1 - 1, -1, -1):
                if str1[j] == str2[j + jump]:
                    continue
                else:
                    jump += lenstr1 - j
                    break
            else:
                print('#{} {}'.format(i + 1, 1))
                break
        else:
            for j in range(lenstr1 - 1, -1, -1):
                if str1[j] == str2[lenstr1 + jump]:
                    jump += lenstr1 - j
                    break
            else:
                jump += lenstr1 + 1

        if lenstr1 + jump >= len(str2):
            print('#{} {}'.format(i + 1, 0))
            break