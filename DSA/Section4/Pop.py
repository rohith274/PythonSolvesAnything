# we will remve node at last of the ll
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

    def pop_list(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while(temp.next != None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    # def append(self, value):  # create new node and add in the last
    # def prepend(self, value):  # create new node and add in the front
    # def insert(self, index, value):  # create new node and add in the index value


mylinkedlist = Section4(11)
mylinkedlist.append(2)
mylinkedlist.append(24)
mylinkedlist.print_list()
mylinkedlist.pop_list()
mylinkedlist.print_list()
