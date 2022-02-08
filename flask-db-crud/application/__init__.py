from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# For the config to work here, I have a local MySQL database running and have already created a flaskdb database in MySQL.
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:MYPASSWORD@localhost:3306/flaskdb"

db = SQLAlchemy(app)

from application import routes