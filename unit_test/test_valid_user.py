# -*- coding: utf-8 -*-
import unittest
from app import is_email_registered

def test_valid_user_registration(self):
    # Check if the user is already registered
    is_registered = is_email_registered("johndoe@example.com")
    
    if is_registered:
        # User is already registered, skip registration
        self.skipTest("User is already registered")
    
    # Proceed with registration
    response = self.client.post('/cadastro', data={
        'fullname': 'John Doe',
        'email': 'johndoe@example.com',
        'password': 'password123'
    })
    
    self.assertEqual(response.status_code, 200)
    self.assertIn('Usuário cadastrado com sucesso!'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
