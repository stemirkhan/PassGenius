from app import app
from flask import render_template
from .func_password import get_passwords_generation, check_password
from .forms import GenerateForm, PasswordVerificationForm


@app.route('/', methods=['GET', 'POST'])
def generate_password():
    form = GenerateForm()
    passwords = []
    if form.validate_on_submit():
        passwords = get_passwords_generation(int(form.input_size.data),
                                             form.numbers.data,
                                             form.lower_let.data,
                                             form.upper_let.data,
                                             form.spec_char.data,
                                             5)

    return render_template('generate_password.html', title='Сгенерировать', passwords=passwords, form=form)


@app.route('/check_password', methods=['GET', 'POST'])
def check_password():
    form = PasswordVerificationForm()
    reliab_percent, reliab, bruteforce_combination = 0, '', 0

    if form.validate_on_submit():
        reliab_percent, reliab, bruteforce_combination = check_password(form.input_password.data)

    return render_template('check_password.html',
                           title='Проверить надежность',
                           reliab_percent=reliab_percent,
                           reliab=reliab,
                           bruteforce_combin=bruteforce_combination,
                           form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='Ошибка 404'), 404
