import unittest
from app import app, BASE_URL, API_KEY

class WeatherAppTests(unittest.TestCase):

    def test_index_get(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_index_post_valid_city(self):
        with app.test_client() as client:
            response = client.post('/', data={'city': 'London'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('London', response.data.decode())
            self.assertIn('Температура', response.data.decode())

    def test_index_post_invalid_city(self):
        with app.test_client() as client:
            response = client.post('/', data={'city': 'InvalidCity'})
            self.assertEqual(response.status_code, 200)
            self.assertIn("Город не найден", response.data.decode())

if __name__ == '__main__':
    unittest.main()
