import pytest
import string
from bs4 import BeautifulSoup


@pytest.mark.parametrize('input_size', [34, 23, 65, 98, 45])
def test_correct_size_pagegen(client, input_size):

    response = client.post('/', data={'input_size': input_size})
    soup = BeautifulSoup(response.data, 'lxml')
    title = soup.find('input', attrs={'id': '0'})

    assert title is not None


@pytest.mark.parametrize('input_size', ['-1', 'jfd', '101', '/.,34', 'fg55', '/*?'])
def test_validation_error_pagegen(client, input_size):

    response = client.post('/', data={'input_size': input_size})
    soup = BeautifulSoup(response.data, 'lxml')
    title = soup.find('p', attrs={'class': 'invalid_messages'})

    assert str(title) == '<p class="invalid_messages">Значение поля от 1 до 100</p>'


@pytest.mark.parametrize('input_password',
                         [_ for _ in string.ascii_lowercase] +
                         [_ for _ in string.ascii_uppercase] +
                         [_ for _ in string.digits] +
                         [chr(_) for _ in range(ord('а'), ord('я'))] +
                         [chr(_).upper() for _ in range(ord('а'), ord('я'))] +
                         [chr(_) for _ in range(ord('\u0627'), ord('\u064a'))])
def test_correct_input_pagecheck(client, input_password):

    response = client.post('/check_password', data={'input_password': input_password})

    assert response.status_code == 200


@pytest.mark.parametrize('input_password',
                         [chr(_).upper() for _ in range(ord('\u3041'), ord('\u3096'))] +
                         [chr(_).upper() for _ in range(ord('\u30A1'), ord('\u30FB'))])
def test_validation_error_input_pagecheck(client, input_password):

    response = client.post('/check_password', data={'input_password': input_password})
    soup = BeautifulSoup(response.data, 'lxml')
    title = soup.find('p', attrs={'class': 'invalid_messages'})

    assert str(title) == '<p class="invalid_messages">Пароль содержит не известные символы</p>'

    assert response.status_code == 200


def test_page_not_found(client):
    response = client.get('/page')

    assert response.status_code == 404
