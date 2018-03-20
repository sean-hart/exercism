def is_isogram(string):
    """ An isogram is a string that has no repeating characters other than
    spaces and dashes.
    """
    # Weeding out the spaces and dashes
    skipchars = [' ', '-']
    for char in skipchars:
        string = string.replace(char, '')

    # A set is a unique list, so by changing the string to a set and
    # comparing to the length of the string, we know if there are any
    # duplicated caracters.
    if len(string.lower()) == len(set(string.lower())):
        return True
    else:
        return False
