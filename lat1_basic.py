from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/age/<string:age>")
def hello_age(age):
    return "I am {} years old" .format(age)

@app.route("/gpa/<float:gpa>")
def hello_gpa(gpa):
    return "My current semester gpa is {:.2f}" .format(gpa)

if __name__=='__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # automatically detect ip from device