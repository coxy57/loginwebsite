from flask import Flask, flash,session, request, render_template, redirect, url_for
import secrets
from functools import wraps

# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57


app = Flask(__name__)

app.secret_key = secrets.token_hex()

users = {
    "discord_id_here" : "helloworld!"
}

b = "made by coxy57"
c = "made by coxy57"

# check if it in session
def validated(func):
    @wraps(func)
    def ok():
        if "user" in session:
            return func()
        else:
            return redirect('/')
    return ok

@app.route('/dashboard')
@validated
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout',methods=['POST'])
@validated
def logout():
    session.pop("user")
    return redirect('/')

@app.route("/",methods=['GET'])
def s():
    if "user" in session:
        return redirect('/dashboard')
    else:
        return render_template("login.html")


@app.route('/login',methods=['POST','GET'])
def admin():
    if request.method == "GET":
        return redirect("/")
    username,password = request.form.values()
    if username in users and users[username] == password:
        session['user'] = username + secrets.token_hex()
        return redirect('/dashboard')
    else:
        flash('Incorrect!')
        return redirect("/")

if __name__ == "__main__":
    if all(x for x in globals() if x in [b,c]):
        app.run(host="127.0.0.1",port=8080)



# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57
# MADE BY coxy57