import pytest

from app import create_app


@pytest.fixture
def app():
    # setup app
    app = create_app()
    app.config.from_object('project.config.TestingConfig')

    # make db can attach the app
    # DO NOT USE `app.app_context().push()` code instead.
    # It is not working properly because the code creates another context.
    # Keep in mind that you have to use context manager.
    with app.app_context():
        # setup db if you have
        # db.create_all()
        # db.session.commit()

        yield app

        # teardown
        #db.session.remove()
        #db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
