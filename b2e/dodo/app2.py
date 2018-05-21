from flask import Flask, jsonify
from .doggy.api import blueprint_api
from .doggy.pages import blueprint_pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_api, url_prefix='/doggy/api')
    app.register_blueprint(blueprint_pages, url_prefix='/doggy/pages')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
