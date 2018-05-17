from flask import Flask, jsonify
from .doggy.api import blueprint_api
from .doggy.pages import blueprint_pages

def create_app():
    app = Flask(__name__, static_folder='./')
    app.register_blueprint(blueprint_api, url_prefix='/doggy/api')
    app.register_blueprint(blueprint_pages, url_prefix='/doggy/pages')

    @app.route('/')
    def root():
        data = dict(say="hello")
        return jsonify(data), 200
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
