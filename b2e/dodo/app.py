from flask import Flask, jsonify

def create_app():
    app = Flask(__name__, static_folder='./')

    @app.route('/')
    def root():
        data = dict(say="hello")
        return jsonify(data), 200
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
