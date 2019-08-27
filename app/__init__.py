__version__ = '0.0.1'

import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # register api
    from . import api
    app.register_blueprint(api.bp)

    return app
