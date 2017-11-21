import unittest

from lostfound.users.models import User
from base import db
from base import BaseTestCase

class TestUserRegistrations(BaseTestCase):
    def test_userCreated(self):
        user = User("john", "admin", "admin@gmail.com","passwords")
        db.session.add(user)
        db.session.commit()
        
        createdUser = User.query.get(1)
        
        self.assertEqual(createdUser.firstname, "John")
        
    def test_userSignIn(self):
        user = User("john", "smith", "john@smith.com","password")
        db.session.add(user)
        db.session.commit()
        
        # Incorrect password
        response = self.client.post("/users/sign_in", data=dict(email="frank@smith.com", password="incorrect"), follow_redirects=True)
        assert 'Incorrect username or password. Please try again.' in response.data
        
        # Correct password
        response = self.client.post("/users/sign_in", data=dict(email="john@smith.com", password="password"), follow_redirects=True)
        assert 'Logged in successfully.' in response.data
        
        
        
        
if __name__ == '__main__':
    unittest.main()