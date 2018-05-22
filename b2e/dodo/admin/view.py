from flask_admin.contrib import sqla
from flask_admin.menu import MenuLink
from flask_security import current_user
from wtforms.fields import PasswordField

from ..utils.gadget import fadmin, db
from ..model.warehouse import Product, Item
from ..model.auth import User, Role

class ProductView(sqla.ModelView):
    can_create = False
    column_list = ('id', 'name', 'expiration_days')

class ItemView(sqla.ModelView):
    column_display_pk = True
    column_list = ('id', 'date_produce', 'product', 'product.name')

class UserView(sqla.ModelView):
    column_exclude_list = ('password',)
    form_excluded_columns = ('password',)
    column_auto_select_related = True

    def is_accessible(self):
        return current_user.has_role('admin')

    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.password2 = PasswordField('New Password')
        return form_class

    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = utils.encrypt_password(model.password2)

class RoleView(sqla.ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

fadmin.add_view(RoleView(Role, db.session, category='Admin'))
fadmin.add_view(UserView(User, db.session, category='Admin'))
fadmin.add_view(ProductView(Product, db.session))
fadmin.add_view(ItemView(Item, db.session))

fadmin.add_link(MenuLink(name='Swagger', url='/apidocs'))
