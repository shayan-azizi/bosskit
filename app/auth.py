from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

digits = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"
special_characters = "!@#$%^&*()_+"

def validate_password (password):
    
    for i in password:
        if i in digits or i in letters or i in special_characters:
            return True
        
    return False

@auth.route("/login", methods = ["GET", "POST"])
def login ():

    return render_template ("login.html", test = "salam")

@auth.route("/logout")
def logout ():
    return "You logged out"

@auth.route("/signup", methods = ["GET", "POST"])
def signup ():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        if password != confirm_password:
            flash ("رمز ها همخوانی ندارند.", category="error")
        
        elif len (username) < 3:
            flash ("نام کاربری باید حداقل 3 کاراکتر باشد.", category="error")
            
        elif len (password) < 8:
            flash ("رمز ورود باید حداقل 8 کاراکتر باشد.", category="error")
            
        elif len (username) > 32:
            flash("نام کاربری باید کمتر از 32 کاراکتر باشد.", category="error")
            
        elif len (password) > 50:
            flash("رمز عبور باید کمتر از 50 کاراکتر باشد.", category="error")
        
        
        elif not validate_password (password) :
            flash("رمز ورود باید حداقل از یک عدد، حرف بزرگ یا کوچک و یک کاراکتر خاص پشتیبانی کند.", category="error")
        
        else:
            flash("حساب کاربری شما ایجاد شد.", category="success")
    
    return render_template ("signup.html")