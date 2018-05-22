# from flasgger import APISpec, Schema, Swagger, fields
from flask_admin import Admin
from flask_marshmallow import Marshmallow
# from flask_security import Security
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
# security = Security()
fadmin = Admin(name='Dodo', template_mode='bootstrap3')
