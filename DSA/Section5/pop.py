class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):  # adds value in the last
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head.next is None:
            return None
        temp = self.tail
        if self.length is 1:
                self.head = None
                self.tail = None    
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            
            return temp


my_dll = DLL(7)
my_dll.append(2)
my_dll.append(4)
my_dll.append(20)
my_dll.pop()
my_dll.printlist()
