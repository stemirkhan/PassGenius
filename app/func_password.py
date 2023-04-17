import random
import string
import re
import math


##########################################################
#        Start function used to generate password        #
##########################################################

def get_passwords_generation(size_password: int,
                             flag_numbers: bool,
                             flag_lower_let: bool,
                             flag_upper_let: bool,
                             flag_spec_char: bool,
                             number_passwords: int) -> list:
    characters_generate = get_alphabet_genpassword(flag_numbers, flag_lower_let, flag_upper_let, flag_spec_char)
    passwords = [password_generation(size_password, characters_generate) for _ in range(number_passwords)]

    return passwords


def password_generation(size_password: int, characters_generate: str) -> str:
    password = ''.join([random.choice(characters_generate) for _ in range(size_password)])

    return password


def get_alphabet_genpassword(flag_numbers: bool,
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

    return characters_generate


##########################################################
#         Start function used to password check          #
##########################################################

def check_password_func(password: str) -> tuple:
    bruteforce_combination = bruteforce_combinations(password)
    password_bit = password_bit_depth(bruteforce_combination)
    reliab_percent = password_strength_percentage(password_bit)
    reliab = password_complexity_reliability(password_bit)
    bruteforce_combination = bring_normal(5, str(bruteforce_combination))

    return reliab_percent, reliab, bruteforce_combination


def password_alphabet_length(password: str) -> int:
    alphabet_length = 0

    regex_length_alphabet = {r'[0-9]': 10, r'[a-z]': 26, r'[A-Z]': 26, r'[ء-ي]': 28,
                             r'(?:[^\w\s]|_)+': 32, r'[а-я]': 33, r'[А-Я]': 33}

    for regex, length in regex_length_alphabet.items():
        if re.search(regex, password):
            alphabet_length += length

    return alphabet_length


def password_bit_depth(bruteforce_combin: int) -> int:
    return int(math.log2(bruteforce_combin))


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
    return password_alphabet_length(password) ** len(password)


def bring_normal(num_unchan_posit: int, bruteforce_combin: str) -> str:
    if len(bruteforce_combin) <= num_unchan_posit:
        bring_normal_species = bruteforce_combin
    else:
        bring_normal_species = f'{bruteforce_combin[:num_unchan_posit]} · ' \
                               f'10^{len(bruteforce_combin[num_unchan_posit:])}'

    return bring_normal_species
