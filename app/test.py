from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'well-secret-password'


class MyForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    starting = SubmitField(label='Starting')
    ending = SubmitField(label='Ending')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():

        if form.starting.data:
            return render_template('1.html')
        elif form.ending.data:
            return render_template('2.html')

        return render_template('test.html', form=form)


    return render_template('test.html', form=form)