import string


def verify(isbn):
    isbn = isbn.replace('-', '')
    if not len(isbn) == 10:
        return False

    total = 0
    multiplier = 0
    for i in isbn[::-1]:
        multiplier += 1
        if multiplier == 1 and i == 'X':
            i = 10
        elif i in string.ascii_letters:
            return False
        else:
            i = int(i)

        total += i * multiplier

    if total % 11 == 0:
        return True
    else:
        return False
