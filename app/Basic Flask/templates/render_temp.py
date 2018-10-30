from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")                       
def indexo():
    name = "python flash workshop"
    return render_template("tmp.html" , name = name)         

if __name__ == "__main__":
    app.run(debug = True)
