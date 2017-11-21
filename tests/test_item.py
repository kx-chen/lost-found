import unittest

from lostfound.items.models import Item
from base import db
from base import BaseTestCase

class FlaskTestCase(BaseTestCase):
    def test_itemCreated(self):
        item = Item("some orang juice", "orang", 1)
        db.session.add(item)
        db.session.commit()
        
        createdItem = Item.query.get(1)
        
        self.assertEqual(createdItem.details, "orang")
        
        # should redirect when user not signed in
        response = self.client.post("/items/new", data=dict(name="orang", details="some orang juice"), follow_redirects=True)
        assert "Sign in" in response.data
        self.assertRedirects(response, "/users/sign_in")
    
    
        
if __name__ == '__main__':
    unittest.main()