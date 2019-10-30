def count_node(x, tree):
    global cnt
    cnt += 1
    if tree[x]:
        for i in tree[x]:
            count_node(i, tree)

for T in range(int(input())):
    E, N = map(int, input().split())
    arr = tuple(map(int, input().split()))
    tree = [[] for i in range(max(arr)+1)]
    cnt = 0
    for i in range(0, E*2, 2):
        tree[arr[i]].append(arr[i+1])
    count_node(N, tree)
    print('#{} {}'.format(T+1, cnt))