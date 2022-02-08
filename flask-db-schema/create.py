from app import db, Users, People

db.drop_all()
db.create_all()

testuser = Users(first_name='Luke', last_name='Benson')
testperson = People(first_name='Jane', last_name='Doe', alive=False, height=2.1)
db.session.add(testperson)
db.session.add(testuser)
db.session.commit()