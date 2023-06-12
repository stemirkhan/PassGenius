from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField
from wtforms.validators import Length, Regexp, DataRequired


class GenerateForm(FlaskForm):
    numbers = BooleanField('Цифры')
    lower_let = BooleanField('Прописные буквы')
    upper_let = BooleanField('Строчные буквы')
    spec_char = BooleanField('Спец. символы')
    submit = SubmitField("СГЕНЕРИРОВАТЬ")
    input_size = StringField(validators=[
        Regexp(r'^(100|[1-9]?[0-9])$', message='Значение поля от 1 до 100'),
        Length(min=1, max=3)])


class PasswordVerificationForm(FlaskForm):
    submit = SubmitField("ПРОВЕРИТЬ")
    input_password = StringField(validators=[
        Regexp(r'^[А-я]|[0-9]|[A-z]|[ء-ي]|(?:[^\w\s]|_)$', message='Пароль содержит не известные символы'),
        Length(min=1, max=100), DataRequired()])
