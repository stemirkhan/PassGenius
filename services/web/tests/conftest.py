import pytest
from app import app


@pytest.fixture()
def _app():
    _app = app
    _app.config.from_object('config.TestingConfig')

    yield _app


@pytest.fixture()
def client(_app):
    return _app.test_client()


@pytest.fixture()
def runner(_app):
    return _app.test_cli_runner()
