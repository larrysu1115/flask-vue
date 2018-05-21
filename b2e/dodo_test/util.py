from dodo.app import create_app
from dodo.utils.gadget import db
import unittest

class DodoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.logger = self.app.logger
        self.db = db
