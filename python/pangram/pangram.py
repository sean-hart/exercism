import string


def is_pangram(sentence):
    sentence = sentence.lower()
    for char in string.ascii_lowercase:
        if char not in sentence:
            return False

    return True


# apparently converting to sets is very expensive
def is_pangram2(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())


if __name__ == '__main__':
    import timeit
    print(timeit.timeit(
        'is_pangram("the quick brown fox jumps over the lazy dog")',
        setup="from __main__ import is_pangram"
        )
    )
    print(timeit.timeit(
        'is_pangram2("the quick brown fox jumps over the lazy dog")',
        setup="from __main__ import is_pangram2"
        )
    )
