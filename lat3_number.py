from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/", )
def index():
    a = round(random.uniform(20,40),2)
    return render_template("number.html", bil=a)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)