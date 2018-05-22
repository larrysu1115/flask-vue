import json
from pprint import pformat
from sqlalchemy.orm import joinedload
from dodo.model.warehouse import Item
from .util import DodoTestCase

class WarehouseTestCase(DodoTestCase):
    def test_read_items(self):
        with self.app.app_context():
            query = self.db.session.query(Item).filter(Item.date_produce < '2017-08-01')
            items = query.options(joinedload(Item.product)).all()

        self.assertEqual(len(items), 2)
        for i in items:
            self.logger.info(i)

    def test_api_items(self):
        rv = self.client.get(
            '/warehouse/item',
            headers={'content-type': 'application/json'})
        data = json.loads(rv.data)
        self.app.logger.info('return object: \n%s', pformat(data))
        self.assertEqual(len(data), 2, 'Should return 2 objects')
