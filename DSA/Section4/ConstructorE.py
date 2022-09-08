class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Section4:
    def __init__(self, value):  # create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # def append(self, value):  # create new node and add in the last
    # def prepend(self, value):  # create new node and add in the front
    # def insert(self, index, value):  # create new node and add in the index value


mylinkedlist = Section4(11)
print(mylinkedlist.head.value)
