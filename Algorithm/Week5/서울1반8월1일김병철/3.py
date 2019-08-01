import sys

sys.stdin = open('input3.txt','r')

def my_count(x):
    collect_dict = {}
    for chr in x:
        if collect_dict.get(chr):
            collect_dict[chr] += 1
        else:
            collect_dict[chr] = 1
    count_dict = list(collect_dict.items())
    for i in range(len(count_dict)-1,0,-1):
        for j in range(i):
            if count_dict[j][1] > count_dict[j+1][1]:
                count_dict[j], count_dict[j+1] = count_dict[j+1], count_dict[j]
            elif count_dict[j][1] == count_dict[j+1][1]:
                if int(count_dict[j][0]) > int(count_dict[j+1][0]):
                    count_dict[j], count_dict[j + 1] = count_dict[j + 1], count_dict[j]
            else:
                continue
    return count_dict[-1][0]+' '+str(count_dict[-1][1])

for i in range(int(input())):
    a,b = input(),input()
    print('#{} {}'.format(i+1,my_count(b)))
