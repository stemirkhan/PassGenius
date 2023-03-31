from app import app
from flask import render_template
from .utils import *
from .forms import GenerateForm


@app.route('/', methods=['GET', 'POST'])
def generate_password():
    form = GenerateForm()
    passwords = []
    if form.validate_on_submit():
        passwords = [
            password_generation(int(form.input_size.data),
                                form.numbers.data,
                                form.lower_let.data,
                                form.upper_let.data,
                                form.spec_char.data)
            for _ in range(5)
        ]

    return render_template('generate_password.html',
                           title='Сгенерировать',
                           passwords=passwords,
                           form=form)
