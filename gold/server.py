from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = "695591aa12"

def getGold(a, b, dmg1, dmg2):
    
    damage = randint(dmg1, dmg2)
    amount = randint(a, b)
    session["gold"] = session["gold"] + amount
    activityString = "Earned " +str(amount)+ " from the " + request.form["building"]+". Took " + str(damage) + " damage"
    
    if session["armor"] > 0:
        if damage > session["armor"]:
            damage -= session["armor"]
            session["armor"] = 0

        else:
            session["armor"] -= damage
            damage = 0

    session["activities"].append(activityString)
    session["health"] = session["health"] - damage
    return render_template("index.html", gold = session["gold"], health = session["health"], armor = session["armor"])


@app.route("/")
def index():
    if "gold" in session:
        print "there's a session already"
        return render_template("index.html", gold = session["gold"], health = session["health"], armor = session["armor"])
    else:
        session["gold"] = 0
        session["activities"] = []
        session["health"] = 100
        session["armor"] = 50
        return render_template("index.html", gold = session["gold"], health = session["health"], armor = session["armor"])

@app.route("/process", methods=['POST'])
def process():
    if request.form["building"] == "cave":
        return getGold(5,10, 0, 10)
    elif request.form["building"] == "farm":
        print "farm!"
        return getGold(10, 20, 0, 5)
    elif request.form["building"] == "house":
        return getGold(2,5, 0, 2)
    elif request.form["building"] == "casino":
        return getGold(-50, 50, 0, 20)
    else:
        return redirect("/")

@app.route("/reset", methods=["Post"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)