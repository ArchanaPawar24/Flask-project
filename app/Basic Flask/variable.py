from flask import Flask
app=Flask(__name__)

@app.route("/variable/<name>")
def String_name(name):
    return 'Hello %s!' % name

@app.route("/variable/<name1>")
def int_name1(name1):
    return 'Hello %i!' % name1

@app.route("/variable/<name2>")
def float_name2(name2):
    return 'Hello %f!' % name2

if __name__ == "__main__":
    app.run(debug = True)
