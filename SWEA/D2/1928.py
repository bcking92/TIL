from base64 import b64decode, b64encode
a = int(input())
for i in range(a):
    b = input()
    print('#{0} {1}'.format(i+1,b64decode(b.encode("utf-8"))))