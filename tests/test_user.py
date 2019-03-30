import unittest

from lostfound.users.models import User
from .base import db, BaseTestCase


class TestUserAuthentications(BaseTestCase):
    def test_userCreated(self):
        user = User("john", "admin", "admin@gmail.com","passwords")
        db.session.add(user)
        db.session.commit()
        
        created_user = User.query.get(1)
        self.assertEqual(created_user.firstname, "John")
        
    def test_userSignIn(self):
        user = User("john", "smith", "john@smith.com","password")
        db.session.add(user)
        db.session.commit()
        
        # Incorrect password
        response = self.client.post("/users/sign_in", data=dict(email="john@smith.com", password="incorrect"), follow_redirects=True)
        assert 'Incorrect username or password. Please try again.' in response.data
        
        # Correct password
        response = self.client.post("/users/sign_in", data=dict(email="john@smith.com", password="password"), follow_redirects=True)
        assert 'Logged in successfully.' in response.data
    
    def test_userRegister(self):
        response = self.client.post("/users/register", data=dict(firstname="", lastname="", email="", password=""), follow_redirects=True)
        assert "Error in the Last Name field - This field is required." in response.data
        
        # Create user with proper fields
        response = self.client.post("/users/register", data=dict(firstname="suk", lastname="mali", email="suk@mali.com", password="sukmali"), follow_redirects=True)
        assert 'Account created, you are now logged in.' in response.data
        
        # Log out
        response = self.client.get("/users/logout", follow_redirects=True)
        assert 'Logged out.' in response.data

        
if __name__ == '__main__':
    unittest.main()
