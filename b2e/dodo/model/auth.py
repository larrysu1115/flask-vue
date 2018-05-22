from flask_security import UserMixin, RoleMixin

from ..utils.gadget import db

class RolesUsers(db.Model):
    __tablename__ = 'auth_roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('auth_user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('auth_role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'auth_role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

class User(db.Model, UserMixin):
    __tablename__ = 'auth_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        'Role',
        secondary='auth_roles_users',
        backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email
