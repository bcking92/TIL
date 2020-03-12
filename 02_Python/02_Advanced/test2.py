import os
  
files = os.listdir('./')
  
for file in files:
    if file[-2:] != 'py':
        name = file
        new_name = file.replace('원래 글자', '바꿀 글자')
        name = os.path.join('./', name)
        new_name = os.path.join('./', new_name)
        os.rename(name, new_name)

        