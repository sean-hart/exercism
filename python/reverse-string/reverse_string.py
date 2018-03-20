def reverse(input=''):
    """ This uses extended slices.  See documentation for details.
    https://docs.python.org/2/whatsnew/2.3.html#extended-slices
    It works by doing [begin:end:step] - by leaving begin and end off and
    specifying a step of -1, it reverses a string.
    """
    return input[::-1]
