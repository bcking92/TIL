arr = [-7, -3, -2, 5, 8]

n = len(arr)

cnt = 0
cases = []
for i in range(1 << n):
    my_sum = 0
    case = []
    for j in range(n):
        if i & (1 << j):
            my_sum += arr[j]
            case.append(arr[j])
    # if not my_sum:
    #     cnt += 1
    cases.append(case)

print(cnt)
print(cases)


