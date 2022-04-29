"""
Write a function, reverse_list, that takes in the head of a linked list as
an argument. The function should reverse the order of the nodes in the
linked list in-place and return the new head of the reversed linked list.
"""


# The linkedList definition
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

"""
n = number of nodes
Time: O(n)
Space: O(1)

"""

#
# def reverse_list(head):
#     current = head
#     prev = None
#     while current is not None:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#     return prev
#

"""
n = number of nodes
Time: O(n)
Space: O(n)

"""


# Recursive
def reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)


print(reverse_list(a))