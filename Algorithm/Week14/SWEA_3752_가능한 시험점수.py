# for T in range(int(input())):
#     N = int(input())
#     temp = 0
#     scores = tuple(map(int, input().split()))
#     stack = [0]
#     new_stack = []
#     for i in range(N):
#         for j in stack:
#             if (j + scores[i]) not in stack:
#                 new_stack.append(j + scores[i])
#         for j in new_stack:
#             stack.append(j)
#         new_stack = []
#     print('#{} {}'.format(T+1, len(stack)))

for T in range(int(input())):
    N = int(input())
    scores = tuple(map(int, input().split()))
    M = 1
    arr = [0] * (N * 100)
    arr[0] = 1
    for i in range(N):
        M += scores[i]
        for j in range(M-1, -1, -1):
            if arr[j]:
                arr[j + scores[i]] = 1
    print('#{} {}'.format(T+1, sum(arr)))
    print(arr)

