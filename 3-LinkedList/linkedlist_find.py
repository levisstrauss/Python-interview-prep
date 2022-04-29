"""
Write a function, linked_list_find, that takes in the head of
a linked list and a target value. The function should return a
boolean indicating whether the linked list contains the target.
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

"""
n = number of nodes
Time: O(n)
Space: O(1)
"""


# def linked_list_find(head, target):
#     if head is None:
#         return False
#     current = head
#     while current is not None:
#         if current.value == target:
#             return True
#         current = current.next
#     return False


"""
n = number of nodes
Time: O(n)
Space: O(n)
"""


def linked_list_find(head, target):
    if head is None:
        return False
    if head.value == target:
        return True
    return linked_list_find(head.next, target)


print(linked_list_find(a, 'A'))
