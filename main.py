from flask import Flask, render_template

from models import storage

app = Flask(__name__)


#the first page the user would see when he visits the site
@app.route('/')
def landing_page():
    return render_template("auth/landing_page.html")


@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/register')
def register():
    return render_template("auth/register.html")


# the page for the user to enter his infos to create his portofolio
@app.route('/informations')
def informations():
    return render_template("main/informations.html")


# the dashboard to see the infos of the user, his work and his offers
@app.route('/dashboard')
def dashboard():
    return render_template("main/dashboard.html")


# the page for the user to see his messages and to message other users
@app.route("/messages")
def messages():
    return render_template("main/messages.html")


# the page for the user to visit after creating an account and filling his infos
@app.route("/home")
def home():
    return render_template("main/home.html")


# the page for the employer to see the list of users that are ready to be employed
@app.route("/feed")
def feed():
    users = storage.all().values()
    return render_template("main/feed.html", users=list(users))
