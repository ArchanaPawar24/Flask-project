from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string '
bootstrap = Bootstrap(app)

class NameForm(Form):
    pname = TextField('what is your name ? ' , validators = [ Required() ])
    
@app.route("/" , methods = ['GET' , 'POST' ])
def index():
    pname = None
    pform = NameForm()
    if pform.validate_on_submit():
        pname = pform.pname.data
        pform.pname.data = " "
    return render_template("form.html" , form = pform , name = pname)

if __name__ == "__main__":
    app.run(debug = True )
