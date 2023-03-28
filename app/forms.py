from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField
from wtforms.validators import Length, Regexp, ValidationError, DataRequired


class GenerateForm(FlaskForm):
    @staticmethod
    def number_range_check(form, field):
        if not ('0' < field.data < '33'):
            raise ValidationError("Значение длины поля не более 32 символов")

    numbers = BooleanField('Цифры')
    lower_let = BooleanField('Прописные буквы')
    upper_let = BooleanField('Строчные буквы')
    spec_char = BooleanField('Спец. символы')
    input_size = StringField(validators=[
        Regexp(r'^[0-9]+$', message='Значение поля должно быть числом'),
        Length(min=1, max=2),
        number_range_check
    ])
    submit = SubmitField("СГЕНЕРИРОВАТЬ")


class PasswordVerificationForm(FlaskForm):
    input_password = StringField(validators=[Length(min=1, max=100), DataRequired()])
    submit = SubmitField("ПРОВЕРИТЬ")
