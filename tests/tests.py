import unittest

from lostfound.users.models import User
from lostfound.appConfig.dbClient import db
from base import BaseTestCase

class FlaskTestCase(BaseTestCase):
    def test_userCreated(self):
        
        user = User("john", "admin", "admin@saasfsdffsdf.com","passwords")
        db.session.add(user)
        db.session.commit()
        
        createdUser = User.query.get(1)
        
        self.assertEqual(createdUser.firstname, "John")
    
    def test_index(self):
        response = self.client.get('/users/sign_in')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()