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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        indexed = self.head
        for _ in range(index):
            indexed = indexed.next
            return indexed


mylinkedlist = Section4(11)
mylinkedlist.append(2)
mylinkedlist.append(24)
mylinkedlist.prepend(21)
mylinkedlist.print_list()
print(mylinkedlist.get(2))

# similarly we can write set method, insert method and remove 
