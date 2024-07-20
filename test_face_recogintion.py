import unittest
from app import app
import os
import io

class TestFlaskEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_compare_faces_endpoint(self):
        data = {
            'known_folder': 'known_images',
            'compared_folder': 'compared_images'
        }
        response = self.app.post('/compare', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("unknown1.jpg", response.get_json())

if __name__ == '__main__':
    unittest.main()
