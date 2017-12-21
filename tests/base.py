from flask_testing import TestCase

from lostfound.appConfig.appFactory import create_app

from lostfound.appConfig.appFactory import db
from lostfound.users.models import User
from lostfound.items.models import Item


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        
        self.app = app
        return app

    def setUp(self):
        db.create_all()
        user = User("john", "smith", "smith@johns.com","password")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def go_to_route(self, route):
        return self.client.get(route)
    
    def login(self):
        response = self.client.post("/users/sign_in", data=dict(email="smith@johns.com", password="password"), follow_redirects=True)
        return response
        