import string
import re

def word_count(phrase):
    count = {}
    temp_phrase = re.sub(r'[^0-9a-zA-Z\']', ' ', phrase)
    for i in temp_phrase.lower().split():
        if i not in count:
            count[i.strip("'")] = 1
        else:
            count[i.strip("'")] += 1
    return count

# def word_count(phrase):
#     counts = {}
#     words = find_words(phrase)
#
#     for word in words:
#         word = word.lower()
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts


def find_words(phrase):
    words = []
    separator_chars = ['\t', '_', ',', ' ']
    word = ""
    index = 0
    for char in phrase:
        if (char in string.ascii_letters
            or char in string.digits
            or (char == '\''
                and phrase[index - 1] in string.ascii_letters
                and phrase[index + 1] in string.ascii_letters)):
                    word += char
        elif char in separator_chars and word != "":
            words.append(word)
            word = ""
        index += 1
    if word != "":
        words.append(word)
    return words
