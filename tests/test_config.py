from flask import current_app

from app import create_app


def test_development_config():
    app = create_app()
    app.config.from_object('app.config.DevelopmentConfig')

    assert app.config['SECRET_KEY'] == 'dev'
    assert current_app is not None
    assert not app.config['TESTING']


def test_testing_config():
    app = create_app()
    app.config.from_object('app.config.TestingConfig')

    assert app.config['SECRET_KEY'] == 'test'


def test_production_config():
    app = create_app()
    app.config.from_object('app.config.ProductionConfig')

    assert app.config['SECRET_KEY'] == 'prod'
    assert not app.config['TESTING']
