# -*- coding: utf-8 -*-
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_valid_user_login(self):
        response = self.client.post('/login', data={
            'email': 'johndoe@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Login bem-sucedido!', response.data) 
if __name__ == '__main__':
    unittest.main()
