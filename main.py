from re import search

from flask import Flask, render_template, request, redirect, url_for

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


@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search = request.form['search'].split()
        if search:
            return redirect(url_for('feed', search=search))
        else:
            return redirect(url_for('home'))
    return render_template("main/home.html")


@app.route("/feed", methods=['GET', 'POST'])
def feed():
    if request.method == "POST":
        # Use request.form to access POST data
        search = request.form.get("search")
        if search:
            users = storage.get_users_by_job_title(search)
        else:
            users = []
    else:
        url_search = request.args.get("search")
        if url_search:
            users = storage.get_users_by_job_title(url_search)
    return render_template("main/feed.html", users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

