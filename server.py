from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "guess my number or perish"

import random

# the route that renders the form to guess the number
@app.route ("/")
def index():
    if "computer_guess" in session:
        print(session["computer_guess"])
    else:
        session["computer_guess"] = random.randint(1,100)
    if "compare" not in session:
        session["compare"] = "none"
        session ["counter"] = 0
    return render_template("index.html", compare = session['compare'], counter = session["counter"])

#the route that procresses the guess
@app.route("/guess", methods=["post"])
def process():
    print(request.form)

    session["counter"] = session ["counter"] + 1 

    if request.form["guess_me"] != "":
        user_guess = int(request.form["guess_me"])
    else:    
        return redirect("/")

    computer_guess = session["computer_guess"]

    if computer_guess > user_guess:
        session["compare"] = "too low!"
    elif computer_guess < user_guess:
        session["compare"] = "too high!"
    else:
        session["compare"] = "perfect"

    print(session["compare"])
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)