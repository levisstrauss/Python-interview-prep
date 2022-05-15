"""
Write a function, insert_node, that takes in the head of a linked list,
a value, and an index. The function should insert a new node with
the value into the list at the specified index. Consider the head
of the linked list as index 0. The function should return the head
of the resulting linked list.

"""
from LinkedList import Node

"""
n = number of nodes
Time: O(n)
Space: O(1)
"""


def insert_node(head, value, index):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    count = 0
    current = head
    while current is not None:
        if count == index - 1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp

        count += 1
        current = current.next
    return head


"""
n = number of nodes
Time: O(n)
Space: O(n)
"""


def insert_node(head, value, index, count=0):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    if head is None:
        return None

    if count == index - 1:
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return

    insert_node(head.next, value, index, count + 1)
    return head
