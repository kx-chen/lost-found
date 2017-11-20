from flask_testing import TestCase

from lostfound.appConfig.appFactory import create_app

from lostfound.appConfig.appFactory import db
from lostfound.users.models import User
from lostfound.items.models import Item


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()