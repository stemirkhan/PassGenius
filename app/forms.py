from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField
from wtforms.validators import Length, Regexp, ValidationError, DataRequired


class GenerateForm(FlaskForm):
    numbers = BooleanField('Цифры')
    lower_let = BooleanField('Прописные буквы')
    upper_let = BooleanField('Строчные буквы')
    spec_char = BooleanField('Спец. символы')
    submit = SubmitField("СГЕНЕРИРОВАТЬ")
    input_size = StringField(validators=[
        Regexp(r'^(30|[1-2]?[1-9])$', message='Значение поля должно быть числом от 1 до 30'),
        Length(min=1, max=2)])


class PasswordVerificationForm(FlaskForm):
    input_password = StringField(validators=[Length(min=1, max=100), DataRequired()])
    submit = SubmitField("ПРОВЕРИТЬ")
