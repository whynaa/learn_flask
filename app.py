from flask import Flask, render_template, redirect, request, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

con = sql.connect('database.db')
print ("opened database sucessfully")

con.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT)')
print("Table created succesfully")
con.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/<username>")
def home(username):
    return render_template("admin_home.html", username = username)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return redirect(url_for("home", username = username))
    
    else:
        username = request.args.get("username")
        return render_template("login.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/result", methods = ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("admin_result.html", result = result)

if __name__=='__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # automatically detect ip from device