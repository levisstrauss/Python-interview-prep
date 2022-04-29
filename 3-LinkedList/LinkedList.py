"""
An introduction to linkedlist algorithms
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node('A')  # head
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


# Print the linkedlist
# def printLinkedlist(head):
#     current = head
#     while current is not None:
#         print(current.value)
#         current = current.next


# Recursively
def printLinkedlist(head):
    if head is None:
        return
    print(head.value)
    printLinkedlist(head.next)


printLinkedlist(a)
