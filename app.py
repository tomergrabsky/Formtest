from flask import *
import csv
from datetime import datetime
import pytz
import os

groupid = -1
tz = pytz.timezone('Israel')
tmstmp = datetime.now(tz)
sex = 0
age = 0
edu = 0
org = 0
job = 0
exp = 0
stress = 0
quest1 = 0
quest2 = 0
isQuest2Delay = 0
quest1_for_who = 0
quest2_for_who = 0


path = 'C:\\temp\\data.csv'

app = Flask(__name__)

data = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route("/")
def home():

    return render_template("index2.html")


@app.route("/group0")
def group0():

    global groupid
    groupid = 0
    global tmstmp
    tmstmp = datetime.now(tz)
    global isQuest2Delay
    isQuest2Delay = -1
    return render_template("details.html", group=groupid)


@app.route("/group1")
def group1():

    global groupid
    groupid = 1
    global tmstmp
    tmstmp = datetime.now(tz)
    return render_template("details.html", group=groupid)


@app.route("/group2")
def group2():

    global groupid
    groupid = 2
    global tmstmp
    tmstmp = datetime.now(tz)
    return render_template("details.html", group=groupid)


@app.route("/group3")
def group3():

    global groupid
    groupid = 3
    global tmstmp
    tmstmp = datetime.now(tz)
    return render_template("details.html", group=groupid)


@app.route("/group4")
def group4():

    global groupid
    groupid = 4
    global tmstmp
    tmstmp = datetime.now(tz)
    return render_template("details.html", group=groupid)


@app.route("/group5")
def group5():

    global groupid
    groupid = 5
    global tmstmp
    tmstmp = datetime.now(tz)
    return render_template("details.html", group=groupid)


@app.route("/group6")
def group6():

    global groupid
    groupid = 6
    global tmstmp
    tmstmp = datetime.now(tz)
    return render_template("details.html", group=groupid)


@app.route('/download')
def downloadfile ():
    path = 'C:\\temp\\data.csv'
    return send_file(path, as_attachment=True)

@app.route('/out')
def out():
    return render_template("out.html")


@app.route('/save_quest1', methods=['POST'])
def save_quest1():

    global quest1
    quest1 = int(request.form.get("quest1"))

    global quest1_for_who
    if groupid == 0 or groupid == 2:
        if quest1 == 1:
            quest1_for_who = 1
        if quest1 == 2:
            quest1_for_who = 2
    print(quest1_for_who)
    if groupid == 1 or groupid == 3:
        if quest1 == 1:
            quest1_for_who = 2
        if quest1 == 2:
            quest1_for_who = 1

    if groupid == 0:
        return render_template("quest2.html", group=groupid)

    if groupid == 1:
        return render_template("quest2-timer1-org-first.html", group=groupid)

    if groupid == 2:
        return render_template("quest2-timer2-client-first.html", group=groupid)

    if groupid == 3:
        return render_template("quest2-timer3-org-first.html", group=groupid)


@app.route('/save_quest2', methods=['POST'])
def save_quest2():

    global isQuest2Delay
    isQuest2Delay = request.form.get("isDelay")

    global quest2
    quest2 = int(request.form.get("quest2"))

    global quest2_for_who
    if groupid == 0 or groupid == 2 or groupid == 4 or groupid == 6:
        if quest2 == 1:
            quest2_for_who = 1
        if quest2 == 2:
            quest2_for_who = 2
    else:
        if quest2 == 1:
            quest2_for_who = 2
        if quest2 == 2:
            quest2_for_who = 1

    return render_template("isinstress.html", group=groupid)


@app.route('/save_stress', methods=['POST'])
def save_stress():

    stress2 = request.form.get("stress2")

    with open(path, mode='a', newline="") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([tmstmp, groupid, sex, age, edu, org, job, exp, stress, quest1, quest1_for_who, quest2,
                         quest2_for_who, stress2, isQuest2Delay])
    file.close()

    return render_template("thanks.html", group=groupid)


@app.route('/save_details', methods=['POST'])
def get_students_list():

    global sex, age, edu, org, job, exp, stress

    sex = request.form.get("sex")
    age = request.form.get("age")
    edu = request.form.get("edu")
    org = request.form.get("org")
    job = request.form.get("job")
    exp = request.form.get("exp")
    stress = request.form.get("stress")

    if groupid == 0 or groupid == 1 or groupid ==2 or groupid == 3:
        if groupid == 0 or groupid == 2:
            return render_template("quest1-client-first.html", group=groupid)
        else:
            return render_template("quest1-org-first.html", group=groupid)

    else:
        global quest1, quest1_for_who
        quest1 = -1
        quest1_for_who = -1

        if groupid == 4:
            return render_template("quest2-timer1-client-first.html", group=groupid)

        if groupid == 5:
            return render_template("quest2-timer2-org-first.html", group=groupid)

        if groupid == 6:
            return render_template("quest2-timer3-client-first.html", group=groupid)


if __name__== "__main__":
    app.run (host='0.0.0.0', port = 80)
