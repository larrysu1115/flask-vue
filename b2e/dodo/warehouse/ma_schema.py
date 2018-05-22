from marshmallow import fields

from ..utils.gadget import ma
from ..model.warehouse import Product, Item

class ProductSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()

class ItemSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    product = fields.Nested(ProductSchema)
    date_produce = fields.Date()

schema_items = ItemSchema(many=True)
