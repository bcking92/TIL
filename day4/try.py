# -*- coding: utf-8 -*-
def input_index():
    num = 0
    try:
        num = int(input('인데스로 사용할 숫자를 입력하세용: '))
    except ValueError as exception :
        raise exception
    else :
        return num
data_list = list(range(1,11))

print(f'data_list: {data_list}')
try :

    num = input_index()

    print (f'[{num}]: {data_list[num]}')
except IndexError as exception :
    print(exception)
except ValueError as exception :
    print(f'{type(exception)}, {exception}')
except Exception as exception :
    print(exception)