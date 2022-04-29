"""
n = length of array a, m = length of array b
Time: O(n*m)
Space: O(min(n,m))

"""


def intersection(a, b):
    result = []
    for item in b:
        if item in a:
            result.append(item)
    return result


# Using a set
"""
n = length of array a, m = length of array b
Time: O(n+m)
Space: O(n)

"""


def intersection(a, b):
    set_a = set(a)
    return [item for item in b if item in set_a]
