# Flask REST API

This is a simple Flask REST API project that uses SQLAlchemy and SQLite. It allows you to define a user model and interact with a local database.

---

## 📂 Files Included

- **api.py** — Main Flask app where the web server and database model are defined.
- **create_db.py** — Script to create the database and tables before running the app.
- **database.db** — SQLite database (auto-created).
- **README.md** — This file!

---

## 🔧 Requirements

- Python 3.x
- pip
- Virtual environment (recommended)

Install necessary packages:

```bash
pip install flask flask_sqlalchemy

🚀 How to Use
Activate your virtual environment (if using one):

bash
source .venv/Scripts/activate  # or .venv\Scripts\activate for PowerShell
Create the database and tables:

bash
python create_db.py
Start the Flask API server:

bash
python api.py
Open your browser and go to:

cpp
http://127.0.0.1:5000/
You’ll see a simple message: Flask REST API.

👤 What the App Does
Sets up a SQLite database with a user model (name, email)

Provides a homepage route (/) for testing the server

Easily extendable for full CRUD functionality

✅ Example User Model
python
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(76), unique=True)
    email = db.Column(db.String(76), unique=True)
📝 Notes
Make sure you run create_db.py before using the app.

You can expand this project to include API routes for adding, viewing, or deleting users.

