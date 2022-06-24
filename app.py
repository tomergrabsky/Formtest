from flask import *
import csv
from datetime import datetime
import pytz
import os


app = Flask(__name__)

data = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route("/")
def home():

    return render_template("index2.html")


@app.route("/timer0")
def timer0():

    return render_template("timer0.html")


@app.route("/timer1")
def timer1():

    return render_template("timer1.html")


@app.route("/timer2")
def timer2():

    return render_template("timer2.html")


@app.route("/timer3")
def timer3():

    return render_template("timer4.html")


@app.route('/download')
def downloadfile ():
    path = 'C:\\temp\\data.csv'
    return send_file(path, as_attachment=True)

@app.route('/out')
def out():
    return render_template("out.html")


@app.route('/save', methods=['POST'])
def get_students_list():

    path = 'C:\\temp\\data.csv'
    tz = pytz.timezone('Israel')
    timenow = datetime.now(tz)

    result = request.form
    sex = request.form.get("sex")
    age = request.form.get("age")
    edu = request.form.get("edu")
    org = request.form.get("org")
    job = request.form.get("job")
    exp = request.form.get("exp")
    stress = request.form.get("stress")
    quest = request.form.get("quest")
    timer = request.form.get("timer")

    print(result)

    with open(path, mode='a', newline="") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([timenow, sex, age, edu, org, job, exp, stress, quest, timer])
        file.close()

    return render_template("hi.html")

if __name__== "__main__":
    app.run (host='0.0.0.0', port = 80)
