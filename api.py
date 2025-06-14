from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating the Flask app
app = Flask(__name__)

# Setting database location (using SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# start the database
db = SQLAlchemy(app)

# Definig user table or model
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # Unique user ID
    name = db.Column(db.String(76), unique=True)        # Name must be unique
    email = db.Column(db.String(76), unique=True)       # Email must be unique

    def __repr__(self):
        return f'USER(name={self.name}, email={self.email})'

# providing Homepage route
@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

# Runing the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
