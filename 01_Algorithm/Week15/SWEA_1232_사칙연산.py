def postorder_search(x, tree):
    x = int(x)
    a = tree[x]
    if a[0] == '*':
        return postorder_search(a[1], tree) * postorder_search(a[2], tree)
    elif a[0] == '/':
        return postorder_search(a[1], tree) // postorder_search(a[2], tree)
    elif a[0] == '+':
        return postorder_search(a[1], tree) + postorder_search(a[2], tree)
    elif a[0] == '-':
        return postorder_search(a[1], tree) - postorder_search(a[2], tree)
    else:
        return int(a[0])

for T in range(10):
    tree = [0]
    for i in range(int(input())):
        tree.append(input().split()[1:])
    print('#{} {}'.format(T+1, postorder_search(1, tree)))
