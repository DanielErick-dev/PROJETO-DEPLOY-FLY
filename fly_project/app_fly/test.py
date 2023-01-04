from django.test import TestCase
class TestHome(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


def soma(numero1, numero2):
    return numero1 + numero2

def testando_soma():
    resultado = soma(1, 1)
    assert resultado == 2
