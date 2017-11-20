import unittest

from lostfound.users.models import User
from base import db
from base import BaseTestCase

class FlaskTestCase(BaseTestCase):
    
    def goToRoute(self, route):
        return self.client.get(route)
        
    def test_sign_in_page(self):
        response = self.goToRoute("users/sign_in")
        self.assertEqual(response.status_code, 200)
        
    def test_register_page(self):
        response = self.goToRoute("users/register")
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()