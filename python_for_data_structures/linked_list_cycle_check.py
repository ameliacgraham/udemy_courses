class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


    def is_cycle(self):
        """Checks if a singly linked list contains a cycle given a head node.

        >>> a = Node("a")
        >>> b = Node("b")
        >>> c = Node("c")
        >>> a.next = b
        >>> b.next = c
        >>> a.is_cycle()
        False


        >>> d = Node("d")
        >>> e = Node("e")
        >>> f = Node("f")
        >>> d.next = e
        >>> e.next = f
        >>> f.next = d
        >>> d.is_cycle()
        True
        """
        seen = set()
        current = self
        while current is not None:
            if current in seen:
                return True
            else:
                seen.add(current)
                current = current.next
        return False

if __name__ == '__main__':
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"