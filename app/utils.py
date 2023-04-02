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
    return int(math.log2(bruteforce_combinations(password)))


def password_complexity_reliability(password_bit: int) -> str:
    if password_bit < 40:
        reliability = 'очень слабая'

    elif password_bit < 60:
        reliability = 'слабая'

    elif password_bit < 80:
        reliability = 'средняя'

    else:
        reliability = 'высокая'

    return reliability


def password_strength_percentage(password_bit: int) -> int:
    if password_bit >= 100:
        return 100
    else:
        return password_bit


def bruteforce_combinations(password: str) -> int:
    return number_password_combinations(password) ** len(password)


def bring_normal(password: str, num_unchan_posit: int) -> str:
    bruteforce_combination = str(bruteforce_combinations(password))

    if len(bruteforce_combination) < num_unchan_posit:
        bring_normal_species = bruteforce_combination
    else:
        bring_normal_species = f'{bruteforce_combination[:num_unchan_posit]} · ' \
                               f'10^{len(bruteforce_combination[num_unchan_posit:])}'

    return bring_normal_species
