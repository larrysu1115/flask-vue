from flasgger import APISpec, Swagger

from ..warehouse.api import get_items
from ..warehouse.ma_schema import ProductSchema, ItemSchema

def setup_swagger(app):
    spec = APISpec(
        title='dodo',
        version='0.0.1',
        plugins=[
            'apispec.ext.flask',
            'apispec.ext.marshmallow'
        ]
    )
    template = spec.to_flasgger(
        app,
        definitions=[ProductSchema, ItemSchema],
        paths=[get_items]
    )
    swag = Swagger(app, template=template)
