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
    q.next = Node(data)
    last = q.next
    if temp:
        q.prev = temp
    else:
        q.prev = q


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
    i = 1
    while i < idx:
        q = q.next
        i += 1
    temp = q.next
    if temp:
        new = Node(x)
        temp.pre = new
        new.next = temp
        new.pre = q
        q.next = new
    if not temp:
        new = Node(x)
        new.pre = q
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
    for i in map(int,input().split()):
        append(i)

    for i in range(M):
        for j in map(int,input().split()):

