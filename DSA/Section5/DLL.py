# we create our constructor
# DLL also have back arrows or previous node address
class Node:
    def __init__(self, value):
        self.value = 7
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


my_dll = DLL(7)
my_dll.printlist()
