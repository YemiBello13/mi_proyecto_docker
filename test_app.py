import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):  # Corregido: debe ser setUp con mayúscula
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hola desde Docker!', response.data)  # Asegúrate que coincide con tu mensaje real

if __name__ == '__main__':
    unittest.main()