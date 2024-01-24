from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# The Zookeeper model should contain a String name, a String birthday, and a list of animals that they take care of using db.relationship().

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    birthday=db.Column(db.String)
    animals = db.relationship('Animal', backref='zookeeper')


# The Enclosure model should contain a String environment (grass, sand, or water), a Boolean open_to_visitors, and a list of animals using db.relationship().
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment=db.Column(db.String)
    open_to_visitors=db.Column(db.Boolean)

    animals = db.relationship('Animal', backref='enclosure')

    def __repr__(self):
        return f''
# The Animal model should contain a String name, a String species, a zookeeper_id, and an enclosure_id. It should be related to zookeepers and enclosures using db.relationship().
# Reminder: You can test any model by itself with pytest testing/models/{modelname}_test.py.
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    species=db.Column(db.String)
    zookeeper_id=db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id=db.Column(db.Integer, db.ForeignKey('enclosures.id'))

