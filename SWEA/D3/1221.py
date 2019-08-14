import sys

sys.stdin = open('input.txt', 'r')

sootja = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

for i in range(int(input())):
    input()
    soo = input().split()
    result = ''
    cntList=[0]*10
    for j in soo:
        cntList[sootja[j]] += 1
    for k,v in sorted(sootja.items(), key=lambda x:x[1]):
        result += (k + ' ') * cntList[v]
    print('#{} {}'.format(i + 1, result))

# idx_list = [ for k in range(10) for j in soo if j == sootja[k]]


