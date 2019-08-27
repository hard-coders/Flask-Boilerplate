import pytest

from app import create_app


@pytest.fixture
def app():
    # setUp
    app = create_app()
    app.config.from_object('app.config.TestingConfig')

    yield app

    # tearDown
    pass


@pytest.fixture
def client(app):
    return app.test_client()
