from flask import Flask , redirect, url_for
app=Flask(__name__)

@app.route("/admin")
def hello_admin():
    return 'Administration area .... \n Guest are not allowed !'

@app.route("/guest/<user>")
def hello_guest(user):
    return 'Guest user %s are not having admin rights !' %user

@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", user=name))
    
if __name__ == "__main__":
    app.run(debug = True)
