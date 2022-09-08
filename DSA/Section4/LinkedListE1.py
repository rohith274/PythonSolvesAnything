# A list is a contiguoues in memory.but linkedlist doesnot have indexes and non-contiguoues which means they are spread at different addresses in memory.  
# In a linked list we have "Head" points to first node and a tail points to last node.
# Every node has it's next node address.  

# BIG O of LinkdList
# Process : Adding new node in last of list
#    O(1) -> simply adding to the last. Doesnot metter how many nodes in the linkedlist
# Process : Removing new node in last of list
#    O(n) -> We should start with head and iterate through the list and check for the tail pointer and the change the tail.
# Process : Adding new node in begining of list
#    O(1) -> simply adding to the front.
# Process : Removing new node in front of list
#    O(1) -> To remove front it is simple.
# Process : Adding new node in middle of list
#    O(n) -> Iterate throuh the list
# Process : Removing new node in middle of list
#    O(n) -> Iterate throuh the list
# Process : Searching in the Linkedlist / Searching LinkedList
#    O(n) -> Iterate thrugh the list

