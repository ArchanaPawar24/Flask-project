from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")
#def tryo():
    #listu = ['archana','Daneil',' Beautiful day in Shrilanka!','Amar','
    #tiger Zinda hai movie was so cool!  '] return
    #render_template("tmp2.html" , listu = listu)

def index():
    user = {'username' : 'Dhiraj!'}
    posts = [
        { 'author' : {'username' : 'Daneil'},
          'body' : 'Beautiful day in Shrilanka!'
          },
        { 'author' : {'username' : 'Amar'},
          'body' : 'tiger Zinda hai movie was so cool! '
          }
        ]
    return render_template('index.html' , user = user , posts = posts)

if __name__ == "__main__":
    app.run(debug = True)
