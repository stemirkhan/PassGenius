import pytest
from app.func_password import *


@pytest.mark.parametrize('size_password', [_ for _ in range(1, 100)])
def test_size_password_generation(size_password):
    password = password_generation(size_password, False, False, False, False)

    assert len(password) == size_password


@pytest.mark.parametrize('flag_numbers, '
                         'flag_lower_let, '
                         'flag_upper_let, '
                         'flag_spec_char', [(True, False, False, False),
                                            (False, True, False, False),
                                            (False, False, True, False),
                                            (False, False, False, True)])
def test_flag_password_generation(flag_numbers, flag_lower_let, flag_upper_let, flag_spec_char):
    password = password_generation(1, flag_numbers, flag_lower_let, flag_upper_let, flag_spec_char)

    if flag_numbers:
        assert re.search('[0-9]', password)
    if flag_lower_let:
        assert re.search('[a-z]', password)
    if flag_upper_let:
        assert re.search('[A-Z]', password)
    if flag_spec_char:
        assert re.search(r'(?:[^\w\s]|_)+', password)


@pytest.mark.parametrize('password, result', [('1', 10), ('a', 26), ('1a', 36),
                                              ('A', 26), ('+', 32), ('1a+', 68),
                                              ('Ъ', 33), ('ъ', 33), ('1a+Ъ', 101)])
def test_number_password_combinations(password, result):
    assert password_alphabet_length(password) == result


@pytest.mark.parametrize('password, result', [('1', 3), ('a', 4), ('1a', 10),
                                              ('A', 4), ('+', 5), ('1a+', 18),
                                              ('Ъ', 5), ('ъ', 5), ('1a+Ъ', 26)])
def test_password_bit_depth(password, result):
    assert password_bit_depth(password) == result


@pytest.mark.parametrize('password_bit, result', [(39, 'очень слабая'), (59, 'слабая'),
                                                  (79, 'средняя'), (100, 'высокая')])
def test_password_complexity_reliability(password_bit, result):
    assert password_complexity_reliability(password_bit) == result


@pytest.mark.parametrize('password_bit, result', [(99, 99), (101, 100)])
def test_password_strength_percentage(password_bit, result):
    assert password_strength_percentage(password_bit) == result


@pytest.mark.parametrize('password, result', [('1', 10), ('a', 26), ('1a', 1296),
                                              ('+', 32), ('1a+', 314432), ('Ъ', 33),
                                              ('1a+Ъ', 104060401)])
def test_bruteforce_combinations(password, result):
    assert bruteforce_combinations(password) == result


@pytest.mark.parametrize('password, num_unchan_posit, result', [('3000000', 3, '100 · 10^5'),
                                                                ('3000000', 8, '10000000')])
def test_bring_normal(password, num_unchan_posit, result):
    assert bring_normal(password, num_unchan_posit) == result
