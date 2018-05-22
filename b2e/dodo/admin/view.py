from flask_admin.contrib import sqla
from flask_admin.menu import MenuLink

from ..utils.gadget import fadmin, db
from ..model.warehouse import Product, Item

class ProductView(sqla.ModelView):
    can_create = False
    column_list = ('id', 'name', 'expiration_days')

class ItemView(sqla.ModelView):
    column_display_pk = True
    column_list = ('id', 'date_produce', 'product', 'product.name')

fadmin.add_view(ProductView(Product, db.session))
fadmin.add_view(ItemView(Item, db.session))

fadmin.add_link(MenuLink(name='Swagger', url='/apidocs'))
