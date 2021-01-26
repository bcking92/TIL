
'''
# 문자열 압축
이중 for문을 돌면서
문자압축길이가 1, 2, 3 ... 일때 어떻게 압축되는지 구하고 최소길이를 리턴
'''

def solution(s):
    answer = 0
    cand = []
    if len(s) > 1:
        for i in range(len(s)//2):
            temp = ''
            temp_num = 1
            temp_s = s[:i+1]
            for j in range(i+1,len(s)+i+1,i+1):
                if s[j:j+i+1] == s[j-i-1:j]:
                    temp_num += 1
                else:
                    if temp_num > 1:
                        temp += f'{temp_num}{temp_s}'
                        temp_num = 1
                        temp_s = s[j:j+i+1]
                    else:
                        temp += temp_s
                        temp_s = s[j:j+i+1]
            cand.append(len(temp))
        answer = min(cand)
    else:
        answer = 1
    return answer