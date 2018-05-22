from flask import Flask, jsonify, url_for
from .doggy.api import blueprint_api
from .warehouse.api import blueprint_api as warehouse_api
import logging.config
from .utils.database import setup_database
from .utils.swagger import setup_swagger
from .utils.gadget import db
from .utils.gadget import fadmin
from .utils.gadget import security
from flask_admin import helpers as admin_helpers
from flask_security import Security, SQLAlchemyUserDatastore
from .model.auth import User, Role

def create_app():
    app = Flask(__name__)
    # setup configuration from ./config/development.py
    app.config.from_object('config.development')
    # setup configuration from a environment variable which contains a file path
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)
    # load logging setting
    logging.config.fileConfig('./config/logging.cfg')

    db.init_app(app)
    fadmin.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    security_app = app.extensions['security']
    @security_app.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=fadmin.base_template,
            admin_view=fadmin.index_view,
            h=admin_helpers,
            get_url=url_for
        )

    setup_database(app)
    app.register_blueprint(blueprint_api, url_prefix='/doggy/api')
    app.register_blueprint(warehouse_api, url_prefix='/warehouse')
    from .admin import view
    setup_swagger(app)

    app.logger.info('application start. __name__ : %s', __name__)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
