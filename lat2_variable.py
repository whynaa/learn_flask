from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello {}!" .format(name)

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