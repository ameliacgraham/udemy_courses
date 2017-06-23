def sum_digits(num):
    """Sum digits of a number using recursion.
    >>> sum_digits(4321)
    10

    """
    if len(str(num)) == 1:
        return num
    else:
        return num % 10 + sum_digits(num/10)

if __name__ == '__main__':
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"