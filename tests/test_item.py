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
        assert "Sign in".encode() in response.data
    
    def test_item_views(self):
        # logged out
        response = self.client.get("/items", follow_redirects=True)
        self.assertEqual(response.status_code, 401)

        self.login()
        response = self.client.get("/items", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert "Your items".encode() in response.data

if __name__ == '__main__':
    unittest.main()