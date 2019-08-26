import os

files = os.listdir('../../../music')

for name in files:

    new_name = os.path.join('../../../music', name[6:])
    name = os.path.join('../../../music', name)
    
    os.rename(name, new_name)
