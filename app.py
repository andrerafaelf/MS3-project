import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_posts")
def get_posts():
    posts = list(mongo.db.posts.find())
    return render_template("posts.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    posts = list(mongo.db.posts.find())
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, posts=posts)

    return redirect(url_for("login"))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    """
    Allow user to edit their account settings.
        - Change Password
        - Delete Account
    """
    user = mongo.db.users.find_one_or_404(
        {"username": session["user"]})

    if session["user"] == username:

        # Update profile function
        if request.method == "POST":

            mongo.db.users.update_one({'username': session['user']},
                                      {'$set': {
                                          'password': generate_password_hash(
                                              request.form.get("password"))
                                      }})

            flash("Account Updated! Log back in to confirm changes.".format(
                    request.form.get("username")))
            session.pop("user")
            return render_template("login.html",
                                   title="Login")

        return render_template("edit_profile.html",
                               user=user,
                               title="Edit Account")

    else:
        # if wrong user
        flash("You do not have permission to view this page")
        return redirect(url_for("recipes",
                                username=session["user"]))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        is_sfw = "on" if request.form.get("is_sfw") else "off"
        post = {
            "category_name": request.form.get("category_name"),
            "post_name": request.form.get("post_name"),
            "user_opinion": request.form.get("user_opinion"),
            "image_url": request.form.get("image_url"),
            "post_source": request.form.get("post_source"),
            "is_sfw": is_sfw,
            "created_by": session["user"]
        }
        mongo.db.posts.insert_one(post)
        flash("Post Successfully Created")
        return redirect(url_for("get_posts"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_post.html", categories=categories)


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    if request.method == "POST":
        is_sfw = "on" if request.form.get("is_sfw") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "post_name": request.form.get("post_name"),
            "user_opinion": request.form.get("user_opinion"),
            "image_url": request.form.get("image_url"),
            "post_source": request.form.get("post_source"),
            "is_sfw": is_sfw,
            "created_by": session["user"]
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash("Post Successfully Edited")
        return redirect(url_for("get_posts"))

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_post.html", post=post, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")
    return render_template("profile.html")


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("create_category.html")


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    return render_template("posts.html", posts=posts)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
