def rec_sum(n):
    """ Recursively sum the digits of an integer.

    >>> rec_sum(4)
    10
    
    """
    # base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)


if __name__ == '__main__':
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"