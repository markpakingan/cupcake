"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    
    __tablename__ = "cupcakes"

    id = db.Column (db.Integer, primary_key = True)
    flavor = db.Column (db.String, nullable = False)
    size = db.Column (db.String, nullable = False)
    rating = db.Column (db.Float, nullable = False)
    image = db.Column (db.String, nullable = False, default = DEFAULT_IMAGE_URL)


    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        
        }
    

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
