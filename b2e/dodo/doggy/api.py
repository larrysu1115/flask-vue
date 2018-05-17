from flask import Blueprint, jsonify
from flask import current_app as app

blueprint_api = Blueprint('doggy_api', __name__)

@blueprint_api.route('/list', methods=['GET'])
def get_list():
    data = [{ 'name': 'dog_aaa' }, { 'name': 'dog_bbb' }]
    return jsonify(data)

@blueprint_api.route('/count', methods=['GET'])
def get_count():
    data = { 'count': 10 }
    return jsonify(data)
