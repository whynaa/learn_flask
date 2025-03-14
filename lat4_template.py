from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/admin")
def hello_admin():
    return render_template("hello.html", name = "admin")

@app.route("/hello/guest/<name>")
def hello_guest(guest):
    return render_template("hello.html", name = guest)

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest"), guest = name)
    
@app.route("/hello/<int:score>")
def mark(score):
    return render_template("mark.html", marks = score)

if __name__=='__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # automatically detect ip from device