import random
import string
import re
import math


def password_generation(size_password: int,
                        flag_numbers: bool,
                        flag_lower_let: bool,
                        flag_upper_let: bool,
                        flag_spec_char: bool) -> str:
    characters_generate = ''

    if flag_numbers or flag_lower_let or flag_upper_let or flag_spec_char:
        if flag_numbers:
            characters_generate += string.digits
        if flag_lower_let:
            characters_generate += string.ascii_lowercase
        if flag_upper_let:
            characters_generate += string.ascii_uppercase
        if flag_spec_char:
            characters_generate += string.punctuation
    else:
        characters_generate += string.digits + string.ascii_lowercase

    password = ''.join([random.choice(characters_generate) for _ in range(size_password)])

    return password


def number_password_combinations(password: str) -> int:
    alphabet_length = 0
    if re.search('[0-9]', password):
        alphabet_length += 10

    if re.search('[a-z]', password):
        alphabet_length += 26

    if re.search('[A-Z]', password):
        alphabet_length += 26

    if re.search(r'(?:[^\w\s]|_)+', password):
        alphabet_length += 32

    return alphabet_length


def password_bit_depth(password: str) -> int:
    alphabet_length = number_password_combinations(password)
    length = len(password)

    return int(math.log2(alphabet_length ** length))