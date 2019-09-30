import sys

sys.stdin = open('input.txt', 'r')

for i in range(int(input())):
    a = input()
    string = ''
    for j in a:
        string += j
        if string == a[len(string):len(string)*2]:
            for k in range(int(len(a)/len(string))-2):
                if string != a[len(string)*(2+k):len(string)*(2+k+1)]:
                    break
            else:
                print('#{} {}'.format(i+1, int(len(a)/len(string))))
                break