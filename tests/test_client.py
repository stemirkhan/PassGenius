import pytest
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


@pytest.mark.parametrize('input_password', ['ي', 'D', 'f', '/', 'Ъ', 'ь'])
def test_input_page_check(client, input_password):

    response = client.post('/check_password', data={'input_password': input_password})

    assert response.status_code == 200


def test_page_not_found(client):
    response = client.get('/page')

    assert response.status_code == 404
