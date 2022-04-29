"""
Write a function, get_node_value, that takes in the head of a linked list
and an index. The function should return the
value of the linked list at the specified index.
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
# def get_node_value(head, index):
#     current = head
#     count = 0
#     while current is not None:
#         if count == index:
#             return current.value
#         count += 1
#         current = current.next
#     return None


"""
n = number of nodes
Time: O(n)
Space: O(n)
"""


# Recursive
def get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.value
    return get_node_value(head.next, index - 1)


print(get_node_value(a, 2))
