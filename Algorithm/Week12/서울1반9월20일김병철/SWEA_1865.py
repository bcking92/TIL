# def permu(arr, n, x):
#     global visited, candi, result, work, my_max
#     if result < my_max:
#         return
#     else:
#         if sum(visited) == n:
#             if result > my_max:
#                 my_max = result
#         else:
#             for i in arr:
#                 if not visited[i]:
#                     if work[x][i]:
#                         visited[i] = 1
#                         result *= work[x][i]/100
#                         permu(arr, n, x + 1)
#                         result /= work[x][i]/100
#                         visited[i] = 0

# def permu(arr, n):
#     global work, my_max
#     stack = [(1, -1, [])]
#     while stack:
#         t, d, x = stack.pop()
#         if d == n - 1:
#             if t > my_max:
#                 my_max = t
#         else:
#             if -1 <= d < n - 1:
#                 for i in arr:
#                     if i not in x:
#                         temp = t * work[d + 1][i] / 100
#                         if temp > my_max:
#                             stack.append((temp, d + 1, x + [i]))

for T in range(int(input())):
    n = int(input())
    arr = [i for i in range(n)]
    visited = [0 for i in range(n)]
    my_max = 0
    work = [tuple(map(int, input().split())) for i in range(n)]
    if n != 1:
        stack = [(1, -1, '')]
        while stack:
            t, d, x = stack.pop()
            if d == n - 1:
                if t > my_max:
                    my_max = t
            else:
                if -1 <= d < n - 1:
                    for i in arr:
                        if str(i) not in x:
                            temp = t * work[d + 1][i] / 100
                            if temp > my_max:
                                stack.append((temp, d + 1, x + str(i)))
        print('#{0} {1:0.6f}'.format(T + 1, my_max * 100))
    else:
        my_max = work[0][0]
        print('#{0} {1:0.6f}'.format(T + 1, my_max))


