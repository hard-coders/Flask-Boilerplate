from flask.cli import FlaskGroup

from app import create_app

app = create_app()
cli = FlaskGroup(app)


@cli.command()
def hello():
    print('Hello, World!')


if __name__ == '__main__':
    cli()
