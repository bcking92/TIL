class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None

head = Node(0)
last = head

def add_to_last(data):
    global head, last
    q = head
    while q.next is not None:
        q = q.next
    q.next = Node(data)
    q.next.prev = q
    last = q.next

array = [1, 2, 3, 4, 5, 6, 7, 8]
for i in array:
    add_to_last(i)

q = head

while q is not None:
    print(q.data, end=" ")
    q = q.next
print()
print("last")
print(last.data)