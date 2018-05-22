from flask import Blueprint, jsonify
from flask import current_app as app
from ..model.warehouse import Item
from sqlalchemy.orm import joinedload
from .ma_schema import schema_items
from ..utils.gadget import db

blueprint_api = Blueprint('warehouse_api', __name__)

@blueprint_api.route('/item', methods=['GET'])
def get_items():
    """
    Item list
    ---
    tags:
      - warehouse
    description: Get all items in the store
    responses:
        200:
            description: list of items
            schema:
                $ref: '#/definitions/Item'
    """
    query = db.session.query(Item).filter(Item.date_produce < '2017-08-01')
    items = query.options(joinedload(Item.product)).all()
    data = schema_items.dump(items)[0]
    return jsonify(data)
