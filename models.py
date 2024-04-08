from app import db

class User(db.Model):
    # Defines a User model with ID, email, and categories fields
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    categories = db.Column(db.String(300), nullable=True)  # Stores user-selected categories

class Affirmation(db.Model):
    # Defines an Affirmation model with ID, category, and text fields
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(300), nullable=False)
