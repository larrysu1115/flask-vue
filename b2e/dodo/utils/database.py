from .gadget import db
from .gadget import security
from ..model.warehouse import Product, Item
from datetime import date

def setup_database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        milk = Product(name='milk', expiration_days=6)
        lunchbox = Product(name='curry lunchbox', expiration_days=3)
        noodle = Product(name='instant noodle', expiration_days=200)
        products = [milk, lunchbox, noodle]

        items = [Item(product=milk, date_produce=date(2017, 8, 1)),
                 Item(product=milk, date_produce=date(2017, 8, 3)),
                 Item(product=lunchbox, date_produce=date(2017, 8, 8)),
                 Item(product=lunchbox, date_produce=date(2017, 7, 31)),
                 Item(product=noodle, date_produce=date(2017, 6, 1)),
                 Item(product=noodle, date_produce=date(2017, 8, 5))]

        db.session.add_all(products)
        db.session.add_all(items)
        db.session.commit()

        ds = security.datastore
        role_admin = ds.find_or_create_role(name='admin', description='Administrator')
        role_user = ds.find_or_create_role(name='user', description='Normal User')
        ds.create_user(email='user@sws9f.org', password='user')
        ds.create_user(email='admin@sws9f.org', password='admin')
        db.session.commit()

        ds.add_role_to_user('user@sws9f.org', 'user')
        ds.add_role_to_user('admin@sws9f.org', 'admin')
        db.session.commit()

