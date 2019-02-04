from flask import render_template, request, jsonify
from app import app


@app.route("/")
@app.route("/index")
def index():
    """route to main homepage"""
    user = {"username":"tukmogi"}
    return render_template("index.html", title="Home", user=user)


@app.route("/about")
def about():
    """route to about page"""
    return render_template("about.html", title="About")


@app.route("/profile")
def profile():
    """route to profile page"""
    user = {"username":"tukmogi", "age":"21"}
    return render_template("profile.html", title="Profile", user = user)


@app.route("/auth/signup", methods=["POST"])
def auth_signup():
    """endpoint to register a user"""
    print(request)
    user_details = "tukmogi"
    # user_details = request.get_json()
    #print(type(user_details))
    #TODO save user details to dbase, returns user details
    if user_details:
        return jsonify({"user details":user_details}), 201
    else:
        return jsonify({"user details":user_details}), 400
