import json
import unittest

from dodo.app import create_app

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.logger = self.app.logger

    def test_api_return_2_obj(self):
        rv = self.client.get(
            '/doggy/api/list',
            headers={'content-type': 'application/json'})
        self.app.logger.info('http response: %s', rv)
        data = json.loads(rv.data)
        self.app.logger.info('return object: %s', data)
        self.assertEqual(len(data), 2, 'Should return 2 objects')

