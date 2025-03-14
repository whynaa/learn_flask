from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/", )
def index():
    report = {
        "suhu" : round(random.uniform(0,45),2),
        "kelembaban": round(random.uniform(0,100),2),
        "tekanan": round(random.uniform(500,1100),2)
    }
    return render_template("indikator.html", report=report)
    # return render_template("indikator.html", **report)
    # to get key, value in report.items()
    # to access suhu we dont need to use "report.suhu", just use "suhu"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)