from flask import blueprints, render_template

auth = blueprints.Blueprint("auth", __name__)

@auth.route("/login")
def login ():
    return render_template ("login.html")

@auth.route("/logout")
def logout ():
    return "You logged out"

@auth.route("/signup")
def signup ():
    return render_template ("signup.html")