from app import app
from flask import render_template
from .func_password import *
from .forms import GenerateForm, PasswordVerificationForm


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


@app.route('/check_password', methods=['GET', 'POST'])
def check_password():
    form = PasswordVerificationForm()
    reliability_percentage = 0
    reliability = ''
    bruteforce_combination = 0
    if form.validate_on_submit():
        password_bit = password_bit_depth(form.input_password.data)
        reliability_percentage = password_strength_percentage(password_bit)
        reliability = password_complexity_reliability(password_bit)
        bruteforce_combination = bring_normal(form.input_password.data, 5)

    return render_template('check_password.html',
                           title='Проверить надежность',
                           reliability_percentage=reliability_percentage,
                           reliability=reliability,
                           bruteforce_combination=bruteforce_combination,
                           form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Ошибка 404'), 404