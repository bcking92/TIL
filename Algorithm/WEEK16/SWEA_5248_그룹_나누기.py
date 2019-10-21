def find_set(x):
    global disjoint_sets
    if x == disjoint_sets[x]:
        return x
    else:
        return find_set(disjoint_sets[x])

def union(x, y):
    global disjoint_sets
    # temp = find_set(y)
    # for i in range(N+1):
    #     if disjoint_sets[i] == temp:
    #         disjoint_sets[i] = find_set(x)
    disjoint_sets[find_set(y)] = find_set(x)



for T in range(int(input())):
    N, M = map(int, input().split())
    arr = tuple(map(int, input().split()))
    disjoint_sets = [i for i in range(N+1)]
    result = 0
    for i in range(0, M*2, 2):
        union(arr[i], arr[i+1])
    for i in range(1, len(disjoint_sets)):
        if disjoint_sets[i] == i:
            result += 1
    print('#{} {}'.format(T+1, result))