def preorder_search(x, arr, l):
    print('node: {0}, level: {1}'.format(x, l))
    if arr[x]:
        if len(arr[x]) == 2:
            preorder_search(arr[x][0], arr, l+1)
            preorder_search(arr[x][1], arr, l+1)
        else:
            preorder_search(arr[x][0], arr, l+1)

def inorder_search(x, arr):
    if arr[x]:
        if len(arr[x]) == 2:
            inorder_search(arr[x][0], arr)
            print(x)
            inorder_search(arr[x][1], arr)
        else:
            inorder_search(arr[x][0], arr)
            print(x)
    else:
        print(x)

def postorder_search(x, arr):
    if arr[x]:
        if len(arr[x]) == 2:
            postorder_search(arr[x][0], arr)
            postorder_search(arr[x][1], arr)
        else:
            postorder_search(arr[x][0], arr)
    print(x)

a = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
arr = [0 for i in range(14)]
for i in range(0, len(a), 2):
    if not arr[a[i]]:
        arr[a[i]] = [a[i+1]]
    else:
        arr[a[i]].append(a[i+1])
for i in range(1, len(arr)):
    if arr[i] == list and len(arr[i]) == 1:
        arr[i].append(0)


print('-------트리--------')
print(arr)
print('--------전위순회--------')
preorder_search(1, arr, 1)
print('--------중위순회--------')
inorder_search(1, arr)
print('--------후위순회--------')
postorder_search(1, arr)

