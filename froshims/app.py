# from flask import Flask, render_template, request
# from cs50 import SQL

# app = Flask(__name__)

# db = SQL("sqlite:///froshims.db")

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Frisbee",
# ]

# # REGISTRANTS = {}

# @app.route("/")
# def index():
#     return render_template("index.html", sports=SPORTS)

# @app.route("/register", methods=["POST"])
# def register():
#     sport = request.form.get("sport")
#     name = request.form.get("name")
#     if not name or sport not in SPORTS :
#         return render_template("failure.html")
#     else:
#         # REGISTRANTS[name] = sport
#         db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
#         return render_template("success.html")

# @app.route("/registrants")
# def registrants():
#     registrants = db.execute("SELECT name, sport FROM registrants")
#     return render_template("registrants.html", registrants=registrants)




# CLIENT-SIDE CODE
from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    sport = request.form.get("sport")
    name = request.form.get("name")
    if not name or not sport:
        return render_template("failure.html")
    else:
        db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
        return render_template("success.html")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT name, sport FROM registrants")
    return render_template("registrants.html", registrants=registrants)
