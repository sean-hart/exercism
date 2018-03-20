import string


def hey(phrase):
    if is_silence(phrase):
        return "Fine. Be that way!"
    elif is_yelling(phrase) and is_question(phrase):
        return "Calm down, I know what I'm doing!"
    elif is_yelling(phrase):
        return 'Whoa, chill out!'
    elif is_question(phrase):
        return "Sure."
    else:
        return "Whatever."


def is_yelling(phrase):
    return phrase.isupper()


def is_question(phrase):
    return phrase.strip(" ").endswith('?')


def is_silence(phrase):
    return (len([x for x in phrase if x not in string.whitespace]) == 0)
