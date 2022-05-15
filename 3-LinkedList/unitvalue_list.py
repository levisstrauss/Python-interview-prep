"""
Write a function, is_univalue_list, that takes in the head of a
linked list as an argument. The function should return a boolean
indicating whether or not the linked list contains exactly one
unique value.


n = number of nodes
Time: O(n)
Space: O(1)
"""


def is_univalue_list(head):
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True


"""
n = number of nodes
Time: O(n)
Space: O(n)
"""


def is_univalue_list(head, prev_val=None):
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list(head.next, head.val)
    else:
        return False
