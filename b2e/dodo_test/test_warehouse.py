from dodo.model.warehouse import Item
from .util import DodoTestCase
from sqlalchemy.orm import joinedload

class WarehouseTestCase(DodoTestCase):
    def test_read_items(self):
        with self.app.app_context():
            query = self.db.session.query(Item).filter(Item.date_produce < '2017-08-01')
            items = query.options(joinedload(Item.product)).all()

        self.assertEqual(len(items), 2)
        for i in items:
            self.logger.info(i)
