from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome', [validators.Length(min=4, max=25)])
    username = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirmar sua Senha', message='Sua senha e confirmação não são iguais')
    ])
    confirm = PasswordField('Digite sua Senha novamente')
    