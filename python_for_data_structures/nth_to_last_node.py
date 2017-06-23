class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def nth_to_last_node(n, head):
    """
    >>> a = Node("a")
    >>> b = Node("b")
    >>> c = Node("c")
    >>> d = Node("d")
    >>> e = Node("e")
    >>> f = Node("f")

    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = e
    >>> e.next = f

    >>> nth_to_last_node(2, a)
    'e'

    >>> nth_to_last_node(4, a)
    'c'
    """
    left_pointer = head
    right_pointer = head

    for i in xrange(n-1):
        if not right_pointer.next:
            raise Error("N is out of range") 
        right_pointer = right_pointer.next

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer.data


if __name__ == '__main__':
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"