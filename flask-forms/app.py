import numbers
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'n7ch5478ynyf3nth745hini4'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    number = IntegerField('Favourite Number')
    dob = DateField('Date of Birth')
    food = SelectField('Favorite Food', choices=[('pizza', 'PIZZA'), ('spaghetti', 'spaghetti'), ('chilli', 'CHILLI')])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        number = form.number.data
        dob = form.dob.data
        food = form.food.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}. Your username is: {number}{dob}{food}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')