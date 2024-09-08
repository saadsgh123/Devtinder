from flask import Flask, render_template

from models import storage

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template("auth/landing_page.html", title='Dev Tinder - Find Your Ideal Tech Talent')


@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/register')
def register():
    return render_template("auth/register.html")


@app.route('/informations')
def informations():
    return render_template("main/informations.html")


@app.route('/dashboard')
def dashboard():
    return render_template("main/dashboard.html")


@app.route("/messages")
def messages():
    return render_template("main/messages.html")


@app.route("/home")
def home():
    return render_template("main/home.html")


@app.route("/feed")
def feed():
    users = storage.all().values()
    return render_template("main/feed.html", users=list(users))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

