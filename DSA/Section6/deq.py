
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueCon:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def printq(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enq(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    def deq(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length ==1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None     
        self.length -=1

my_queue = QueueCon(4)
my_queue.enq(2)
my_queue.printq()
print('de-queue')
my_queue.deq()
my_queue.printq()



