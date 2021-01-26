'''
# 문자열 재정렬
정렬 후 숫자와 문자가 구분되는 부분에서 잘라서 문자는 그대로 출력, 숫자는 합을 구해서 출력
'''

def solution(s):
    sorted_s = sorted(s)
    for i in range(len(sorted_s)):
        if not sorted_s[i].isdigit():
            return f'{"".join(sorted_s[i:])}{sum(map(int,sorted_s[:i]))}'
        
print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))
