# from flask_security import SQLAlchemyUserDatastore

from .gadget import db
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
