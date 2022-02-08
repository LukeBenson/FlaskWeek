from application import db
from application.models import Games

db.drop_all()
db.create_all()