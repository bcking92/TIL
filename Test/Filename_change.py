## 파일명 일괄 변경하기 ##


# os 모듈을 호출한다.
import os

files = os.listdir('./')

for name in files:
    if name[-2:] != 'py' and name[-3:] != 'Bin':
        temp = name
        new_temp = name[3:]
        # name = os.path.join('./', temp)
        # new_name = os.path.join('./', new_temp)
        os.rename(temp, new_temp)

    ## 끝 ## 
