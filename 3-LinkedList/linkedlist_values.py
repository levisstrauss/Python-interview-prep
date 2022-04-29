"""
Write a function, linked_list_values, that takes in the head of a
linked list as an argument. The function should return a list containing
all values of the nodes in the linked list.

if n is the numbers of nodes
Time O(n) is based on the data we are operating on
Space O(n) is based on the output of the data we are operating on
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


# def linked_list_values(head):
#     values = []
#     current = head
#     while current is not None:
#         values.append(current.val)
#         current = current.next
#     return values


# Recursive
def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values


def fill_values(head, values):
    if head is None:
        return
    values.append(head.value)
    fill_values(head.next, values)


print(linked_list_values(a))
