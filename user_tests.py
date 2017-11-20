import unittest
from tests.base import BaseTestCase
from lostfound.users.models import User
from lostfound.appConfig.dbClient import db

class FlaskTestCase(BaseTestCase):
    def test_userCreated(self):
        db.create_all()
        user = User("admin", "admin", "admin@saasfsdffsdf.com","passwords" )
        db.session.add(user)
        db.session.commit()
        
        createdUser = User.query.get(1)
        
        self.assertEqual(createdUser.firstname, "Admin")
    
    def test_index(self):
        response = self.client.get('/users/sign_in')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()