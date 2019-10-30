class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

def insert(idx, data):
    global head, tail
    q = head
    i = 0
    while i < idx:
        q = q.next
        i += 1
        if q.next is None:
            break
    if q.next is None:
        q.next = Node(data)
        q.next.prev = q
        tail = q.next
    else:
        temp = q.next
        q.next = Node(data)
        q.next.prev = q
        q.next.next = temp
        temp.prev = q.next


for T in range(int(input())):
    head = Node('list')
    tail = head
    N, M = map(int, input().split())
    cnt = 0
    for i in map(int, input().split()):
        insert(0 + cnt, i)
        cnt += 1
    for i in range(M-1):
        b = tuple(map(int, input().split()))
        q = head.next
        idx = 0
        while q.data <= b[0]:
            q = q.next
            idx += 1
            if q is None:
                break
        for j in range(N):
            insert(idx + j, b[j])

    t = tail
    print('#{}'.format(T+1), end=' ')
    for i in range(10):
        print(t.data, end=' ')
        t = t.prev
    print()