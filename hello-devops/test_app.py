# test_app . py
import unittest
from app import app
# For a simple example , we simply test True .
class TestApp(unittest.TestCase):
    def test_home_route(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
