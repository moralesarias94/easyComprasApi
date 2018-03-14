
import unittest
import json
import requests

class TestRemoteItems(unittest.TestCase):
    def testGetLatestItems(self):
        items = [{"_id": "12345", "nombre": "Leche"}]
        url = 'https://easycompras-api.herokuapp.com/productos'
        params = {'where' : json.dumps({'nombre': 'Leche'})}
        producto = requests.get(url, params=params).json()['_items'][0]
        self.assertEqual(items[0]['nombre'], producto['nombre'])

if __name__ == '__main__':
    unittest.main()