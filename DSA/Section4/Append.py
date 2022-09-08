# we will create a new node at the end of the linked list
# we will change last item's address and tail.
# we have edge case when linke dlist is empty.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Section4:
    def __init__(self, value):  # create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # def append(self, value):  # create new node and add in the last
    # def prepend(self, value):  # create new node and add in the front
    # def insert(self, index, value):  # create new node and add in the index value


mylinkedlist = Section4(11)
mylinkedlist.append(2)
mylinkedlist.append(24)
mylinkedlist.print_list()
