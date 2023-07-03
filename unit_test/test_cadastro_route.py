import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_cadastro_route(self):
        response = self.client.get('/cadastro')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Cadastre sua conta</h2>', response.data)

if __name__ == '__main__':
    unittest.main()
