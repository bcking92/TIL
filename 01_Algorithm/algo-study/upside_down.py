def solution(input):
    zero, one, now = 0, 0, -1
    for i in input:
        if i == '0':
            if now != '0':
                zero += 1
                now = '0'
            else:
                continue
        else:
            if now!= '1':
                one += 1
                now = '1'
            else:
                continue
    return min(zero, one)

print(solution('0001100100111'))

