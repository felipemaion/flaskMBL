# from app.extensions import db

# class Manager(db.Model):
#     __tablename__ = 'manager'
#     manager_id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(100))
#     password = db.Column(db.String(255))

#     def __repr__(self):
#         return f'<Manager "{self.title}">'

import hashlib
from app.extensions import db


class Manager(db.Model):
    __tablename__ = "manager"
    manager_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(255))  # Storing hashed password

    def __repr__(self):
        return f'<Manager "{self.user_name}">'

    @property
    def _password(self):
        return self._password

    @_password.setter
    def _password(self, _password):
        # Hash the password before storing it
        self.password = hashlib.sha256(_password.encode()).hexdigest()


# Register event listener to hash password before insertion
@db.event.listens_for(Manager, "before_insert")
def hash_password_before_insert(mapper, connection, target):
    if target.password:
        target.password = hashlib.sha256(target.password.encode()).hexdigest()


# Register event listener to hash password before update
@db.event.listens_for(Manager, "before_update")
def hash_password_before_update(mapper, connection, target):
    if target.password:
        target.password = hashlib.sha256(target.password.encode()).hexdigest()
