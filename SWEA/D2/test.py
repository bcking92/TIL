def mycalc(x):
    c = '0'
    result = 0
    for i in x +' ':
        if i.isdigit():
            c += i
        else:
            result += int(c)
            c = '' + i
    return result

