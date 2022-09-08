
def reverse(self):
    # we usually switch head and tail then reverse all arrows.
    temp = head
    head = tail
    tail = temp
    # for _ in range() -> we use i if use the i value inside the llop ether we can use_ for iterating
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after
        

