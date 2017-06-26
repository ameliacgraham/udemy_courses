
def reverse(s):
    """
    Reverse a string using recursion.

    >>> reverse('abc')
    'cba'

    >>> reverse('hello')
    'olleh'
    """

    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]

if __name__ == '__main__':
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"