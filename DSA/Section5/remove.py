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

    def prepend(self, value):  # add value in the beginning of dll
        new_node = Node(value)
        if self.length is 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length is 0:
            return None
        temp = self.head

        if self.length is 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index ==0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)   

        temp.next.prev = temp.prev
        temp.prev.next = temp.next    
        temp.next = None
        temp.prev = None

        self.length -=1
        return temp    

my_dll = DLL(7)
my_dll.append(2)
my_dll.append(4)
my_dll.append(20)
my_dll.pop()
my_dll.prepend(1)
my_dll.prepend(2)
my_dll.popfirst()
my_dll.printlist()
print("value at given index is = ")
print(my_dll.get(1))
my_dll.insert(1, 200)
my_dll.printlist()
my_dll.remove(4)
print("Altered after Remove function")
my_dll.printlist()

