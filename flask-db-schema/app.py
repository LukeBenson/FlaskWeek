from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# For the config to work here, I have a local MySQL database running and have already created a flaskdb database in MySQL.
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:MYPASSWORD@localhost:3306/flaskdb"

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(747), nullable=False)
    last_name = db.Column(db.String(747), nullable=False)
    alive = db.Column(db.Boolean, default=True)
    height = db.Column(db.Float)

if __name__ == '__main__':
    app.run(debug=True)