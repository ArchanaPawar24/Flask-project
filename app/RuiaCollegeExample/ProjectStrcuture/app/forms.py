from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class NameForm(Form):
    name = TextField('what is u r name ? ' , validators = [ Required() ])


