
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


my_queue = QueueCon(4)
my_queue.printq()
