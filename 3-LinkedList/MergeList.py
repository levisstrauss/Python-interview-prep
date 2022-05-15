"""
Write a function, merge_lists, that takes in the head of two sorted linked
lists as arguments. The function should merge the two lists together into
single sorted linked list. The function should return the head of the merged
linked list.

"""
from LinkedList import Node

"""
n = length of list 1
m = length of list 2
Time: O(min(n, m))
Space: O(1)

"""


def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    current_1 = head_1
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next

    if current_1 is not None: tail.next = current_1
    if current_2 is not None: tail.next = current_2

    return dummy_head.next


"""
n = length of list 1
m = length of list 2
Time: O(min(n, m))
Space: O(min(n, m))

"""


# Recursive
def merge_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    if head_1.val < head_2.val:
        next_1 = head_1.next
        head_1.next = merge_lists(next_1, head_2)
        return head_1
    else:
        next_2 = head_2.next
        head_2.next = merge_lists(head_1, next_2)
        return head_2
