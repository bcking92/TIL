class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value 
        self.next = None

class Linked_List:
    def __init__(self):
        self.header = None
        self.tail = None

    def add(self, value):
        if self.tail == None:
            new_node = Node(value)
            self.header = new_node
            self.tail = new_node
            return self.tail.value
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return new_node.value

    def remove(self, index):
        if self.header:
            now = self.header
            for i in range(index):
                now = now.next
            now_next = now.next
            now_prev = now.prev
            now_prev.next = now.next
            now_next.prev = now.prev
    
    def get(self, index):
        now = self.header
        for i in range(index):
            now = now.next
        if now == None:
            return 'out of index'
        return now.value
    
    def __repr__(self):
        now = self.header
        result = '['
        while now.next != None:
            result += f'{now.value},'
            now = now.next
        result += f'{now.value}]'
        return result


my_list = Linked_List()
my_list.add(2)
my_list.add(1)
my_list.add(3)
my_list.add(2)
my_list.remove(2)

    
print(my_list)
    
