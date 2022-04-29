"""
Write a function, sum_list, that takes in the head of a linked
list containing numbers as an argument. The function should return
the total sum of all values in the linked list.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node(2)  # head
b = Node(45)
c = Node(100)
d = Node(3)

a.next = b
b.next = c
c.next = d

"""
n = number of nodes
Time: O(n)
Space: O(1)
"""

# def sum_list(head):
#     summation = 0
#     current = head
#     while current is not None:
#         summation += current.value
#         current = current.next
#     return summation


# Recursive

"""
n = number of nodes
Time: O(n)
Space: O(n)
"""


def sum_list(head):
    if head is None:
        return 0
    return head.value + sum_list(head.next)


print("The sum of all element is:", sum_list(a))
