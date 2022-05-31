import click
from flask.cli import with_appcontext
from apps import db
from apps.authentication.models import user_loader ,request_loader

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
