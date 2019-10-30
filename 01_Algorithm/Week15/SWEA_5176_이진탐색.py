def binary_search_tree(x, tree):
    global tree2, cnt
    if tree[x]:
        if len(tree[x]) == 2:
            binary_search_tree(tree[x][0], tree)
            tree2[x] = cnt
            cnt += 1
            binary_search_tree(tree[x][1], tree)
        elif len(tree[x]) == 1:
            binary_search_tree(tree[x][0], tree)
            tree2[x] = cnt
            cnt += 1
    else:
        tree2[x] = cnt
        cnt += 1
for T in range(int(input())):
    N = int(input())
    tree = [[] for i in range(N+1)]
    tree2 = [0 for i in range(N+1)]
    cnt = 1
    for i in range(2, N+1):
        tree[i//2].append(i)
    binary_search_tree(1, tree)
    print('#{} {} {}'.format(T+1, tree2[1], tree2[N//2]))