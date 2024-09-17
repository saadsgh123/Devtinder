from re import search

from flask import Flask, render_template, request, redirect, url_for, flash

from models import storage

app = Flask(__name__)
from models import storage


@app.route('/')
def landing_page():
    return render_template("auth/landing_page.html", title='Dev Tinder - Find Your Ideal Tech Talent')


@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/register')
def register():
    return render_template("auth/register.html")


@app.route('/informations', methods=['GET', 'POST'])
def informations():
    user_id = ""
    if user_id == "":
        if request.method == "POST":
            storage.create_user_profile(
                username=request.form.get('first-name'),
                email=request.form.get('email'),
                password=request.form.get('last-name'),
                job_title=request.form.get('job-title'),
                country=request.form.get('address'),
                city=request.form.get('city'),
            )
            return redirect(url_for('home'))
    else:
        user = storage.get_user_by_id(user_id)
        return render_template("main/informations.html", user=user)


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
    users = []
    if request.method == "POST":
        search = request.form.get("search").strip()
        if search:
            users = storage.get_users_by_job_title(search)
            # Check if users is empty, not None
            if not users:
                flash("No users found", category="error-message")
        else:
            flash("Search field cannot be empty!", "error-message")
    else:
        if request.method == "GET":
            url_search = request.args.get("search")
            if url_search:
                url_search = url_search.strip()
                users = storage.get_users_by_job_title(url_search)
                if not users:
                    flash("No users found", category="error-message")
            else:
                return redirect(url_for('home'))
    return render_template("main/feed.html", users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

