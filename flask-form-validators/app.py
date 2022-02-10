from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # We will only use StringField and SubmitField in our simple form.
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY' #Configure a secret key for CSRF protection.

class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        for banned in ['admin', 'root']:
            if username.data.lower() == banned:
                raise ValidationError("can't have this username")
        for character in username.data.lower():
            if character in ['$', '£', '@']:
                raise ValidationError("can't have special characters in your username")

@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form = form, username=username)
    else:
        return render_template('home.html', form = form, username="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')