from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<name>")
def hello_guest(guest):
    return "hello {} as Guest" .format(guest)

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest"), guest = name)

if __name__=='__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # automatically detect ip from device