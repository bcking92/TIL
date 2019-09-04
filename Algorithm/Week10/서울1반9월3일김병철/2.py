class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#
# class LinkedList:
#     def __init__(self):
#         temp = Node('head')
#         self.head = temp
#         self.last = temp
#
#     def append(self, data):
#         temp = Node(data)
#         self.last.next = temp
#         temp.prev = self.last
#         self.last = temp



# ad = Linked_List()

# print(ad)

# a = Node('my_list')
# head = a
# last = a
# last = head

def append(data):
    global head, last
    q = head
    temp = 0
    while q.next is not None:
        temp = q
        q = q.next
    a = Node(data)
    q.next = a
    last = a
    if temp:
        a.prev = q
    else:
        a.prev = q


# def delete(x):
#     global head
#     q = head
#     while q.next.data != x:
#         q = q.next
#     temp = q.next.next
#     temp.prev = q
#     del q.next
#     q.next = temp


def insert(idx, x):
    global head, last
    q = head
    i = 0
    while i < idx:
        q = q.next
        i += 1
    temp = q.next
    if temp:
        new = Node(x)
        temp.prev = new
        new.next = temp
        new.prev = q
        q.next = new
    if not temp:
        new = Node(x)
        new.prev = q
        q.next = new
        last = new

# head = Node('mylist')

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in arr:
#     append(i)
#
# #
# delete(3)
# insert(3, 3)
# insert(11, 200)
#
#
# k = head
#
# while k is not None:
#     print('pre data {} next'.format(k.data))
#     k = k.next


for T in range(int(input())):
    N, M = map(int, input().split())
    a = Node('mylist')
    head = a
    last = a
    cc = head
    for i in map(int, input().split()):
        append(i)
        # cc = cc.next
        # print(cc.prev.data)

    for i in range(M-1):
        b = list(map(int, input().split()))
        q = head
        q = q.next
        i = 0
        while q is not None and q.data < b[0]:
            q = q.next
            i += 1
        # if i == 1:
        #     i = 0
        if q is not None:
            if q.prev.data == 'mylist':
                for j in range(len(b)):
                    insert(i+j, b[j])
            else:
                for j in range(len(b)):
                    insert(i+j+1, b[j])
        else:
            for j in range(len(b)):
                insert(i+j, b[j])

    q = head

    while q is not None:
        print(q.data, end=' ')
        q = q.next
    print()
