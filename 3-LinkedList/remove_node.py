"""
Write a function, remove_node, that takes in the head of a linked list
and a target value as arguments. The function should delete the node
containing the target value from the linked list and return the head of
the resulting linked list. If the target appears multiple times in the
linked list, only remove the first instance of the target in the list.

"""

"""
n = number of nodes
Time: O(n)
Space: O(1)
"""


def remove_node(head, target_val):
    if head.val == target_val:
        return head.next

    current = head
    prev = None
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head


"""
n = number of nodes
Time: O(n)
Space: O(n)

"""


def remove_node(head, target_val):
    if head is None:
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node(head.next, target_val)
    return head
