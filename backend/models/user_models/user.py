from app import db


class UserModel(db.Model):
    """This class creates the models for a user object"""

    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(80))
    last_name = db.Column('last_name', db.String(80))
    username = db.Column('username', db.String(80), unique=True, nullable=False)
    email = db.Column('email', db.String(80), nullable=False)
    short_description = db.Column('short_description', db.String(80))
    join_date = db.Column('join_date', db.TIMESTAMP)
    active = db.Column('active', db.Boolean, default=False, nullable=False)
    status = db.Column('status', db.String(80))

    def __init__(self, new_user):
        """This method is used to initialize the user objects"""

        self.first_name = new_user['first_name']
        self.last_name = new_user['last_name']
        self.username = new_user['username']
        self.email = new_user['email']
        self.short_description = new_user['short_description']
        self.join_date = new_user['join_date']
        self.active = new_user['active']
        self.status = new_user['status']

    def __repr__(self):
        """This method returns a string representation of the user object"""

        return 'UserModel %r' % self.username

    def json(self):
        """This method returns a json representation of the user object"""

        return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'username': self.username,
                'emai': self.email, 'short_description': self.short_description, 'join_date': self.join_date,
                'active': self.active, 'statue': self.status, }

    def save_to_db(self):
        """This methods saves the changes made to a user object and commits those changes to the database"""

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """This methods deletes a user object and commits those changes to the database"""

        db.session.delete(self)
        db.session.commit()


db.create_all()
db.session.commit()















