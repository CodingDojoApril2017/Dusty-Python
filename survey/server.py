from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "123abc"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    count = 0
    name1 = request.form["name"]
    location1 = request.form["location"]
    language1 = request.form["language"]
    comment1 = request.form["comment"]
    if len(request.form["name"]) < 1:
        flash("name cannot be blank")
        count += 1
    if len(request.form["comment"]) < 1:
        flash("comment cannot be blank")
        count += 1
    elif len(comment1) > 255:
        flash("comment is too long")
        count += 1
    if count > 0:
        return redirect("/")

    return render_template("result.html", name = name1, location = location1, language=language1, comment=comment1)
app.run(debug=True)
    