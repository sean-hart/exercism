import string as s

# NOTE: TRY RECURSION!

def decode(string):
    if string == '':
        return ''
    uncompressed_string = ''
    digits = ''
    for char in string:
        if char in (s.digits):
            digits = f'{digits}{char}'
        else:
            if digits == '':
                digits = 1
            uncompressed_string = f'{uncompressed_string}{char * int(digits)}'
            digits = ''
    return uncompressed_string

def encode(string):
    if string == '':
        return ''
    compressed_string = ''
    current_letter = string[0]
    current_count = 0
    for letter in string:
        if letter == current_letter:
            current_count += 1
        else:
            if current_count == 1:
                current_count = ''
            compressed_string = f'{compressed_string}{current_count}{current_letter}'
            current_letter = letter
            current_count = 1
    if current_count == 1:
        current_count = ''
    compressed_string = f'{compressed_string}{current_count}{current_letter}'
    return compressed_string
