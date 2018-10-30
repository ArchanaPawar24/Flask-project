from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")

def dicto():
    dict={1:'archana',2:'vinoti',3:'shraddha'}
    return render_template("tmp1.html" , dict = dict)

if __name__ == "__main__":
    app.run(debug = True)
