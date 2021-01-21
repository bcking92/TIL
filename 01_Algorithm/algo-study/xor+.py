def solution(input):
    numbers = list(map(int, input))
    result = 0
    for i in range(1, len(numbers)):
        if i == 1:
            a = numbers[i-1] + numbers[i]
            b = numbers[i-1] * numbers[i]
            if a > b:
                result = a
            else:
                result = b
        else:
            a = result + numbers[i]
            b = result * numbers[i]
            if a > b:
                result = a
            else:
                result = b
    return result

print(solution('02984'))
                

    
