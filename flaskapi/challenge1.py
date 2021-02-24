#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/secret/<name>")
def secret(name):
    return f"You have reached the lair {name}\n"
@app.route("/boring/<name>")
def boring(name):
    return f"Why you so...basic? {name}\n"
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker2.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nn"): # if nm was assigned via the POST
            user = request.form.get("nn") # grab the value of nm from the POST
            if user == "JillyWilly":
                return redirect(url_for("secret", name = user))
        else: # if a user sent a post without nm then assign value defaultuser
            user = "Noname"
            return redirect(url_for("boring", name = user))
    # GET would likely come from a user interaacting with a browser
    elif request.method == "GET":
        if request.args.get("nn"): # if nm was assigned as a parameter=value
            user = request.args.get("nn") # pull nm from localhost:5060/login?nm=larry
            if user == "JillyWilly":
                return redirect(url_for("secret", name = user))
        else: # if nm was not passed...
            user = "Noname" # ...then user is just defaultuser
            return redirect(url_for("boring", name = user))
    return redirect(url_for("success", name = user)) # pass back to /success with val for name
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

