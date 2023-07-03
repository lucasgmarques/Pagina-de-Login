import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_invalid_user_registration_missing_fields(self):
        response = self.client.post('/cadastro', data={
            'fullname': 'John Doe',
            'email': '',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Por favor, preencha todos os campos.', response.data)

if __name__ == '__main__':
    unittest.main()
