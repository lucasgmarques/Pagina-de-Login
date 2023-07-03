# -*- coding: utf-8 -*-
import unittest
from app import app, is_email_registered

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_cadastro_route(self):
        response = self.client.get('/cadastro')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Cadastre sua conta</h2>', response.data)

    def test_login_route(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Esqueceu a senha?', response.data)

    def test_invalid_user_registration_missing_fields(self):
        response = self.client.post('/cadastro', data={
            'fullname': 'John Doe',
            'email': '',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Por favor, preencha todos os campos.', response.data)

    def test_invalid_user_registration_invalid_email(self):
        response = self.client.post('/cadastro', data={
            'fullname': 'John Doe',
            'email': 'invalidemail',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Por favor, forneça um email válido.'.encode('utf-8'), response.data)

    def test_valid_user_registration(self):
        # Checa se o usuário já está cadastrado
        is_registered = is_email_registered("johndoe@example.com")
        
        if is_registered:
            # Se o usuário já está cadastrado, pular essa etapa
            self.skipTest("Este e-mail já está cadastrado.")
        
        # Proceder com o registro da conta
        response = self.client.post('/cadastro', data={
            'fullname': 'Michael',
            'email': 'michael@example.com',
            'password': 'password123'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Usuário cadastrado com sucesso!'.encode('utf-8'), response.data)


if __name__ == '__main__':
    unittest.main()
