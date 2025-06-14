from api import app, db

# Creating database tables from models
with app.app_context():
    db.create_all()
