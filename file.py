import os

# print(os.listdir())

# os.rename('file.py', 'hi.py')

# print(os.listdir())

# os.system('touch a.txt')

# 100번 반복하여 파일을 생성

# os.system('cd report')

os.chdir('report')

# for i in range(200) :
    # os.system(f'touch report{i}.txt')   # python 3.6부터 적용된 문법

files = os.listdir()

# for name in files :
#     os.rename(name, "samsung_" + name)

for name in files :
    rep = name.replace("samsung", "SSAFY")
    os.rename(name, rep)

