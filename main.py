from re import search

from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy.sql.functions import current_user

from models import storage

app = Flask(__name__)
from models import storage

app.secret_key = 'your_secret_key'


@app.route('/')
def landing_page():
    return render_template("auth/landing_page.html", title='Dev Tinder - Find Your Ideal Tech Talent')


@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        country = request.form['country']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            new_user = storage.create_user_profile(username, country, email, password)
            session['user_id'] = new_user.id
            return redirect(url_for('informations'))
    return render_template("auth/register.html")


@app.route('/informations/', methods=['GET', 'POST'])
def informations():
    user_id = session.get('user_id')
    curr_user = storage.get_user_profile(user_id)
    if request.method == 'POST':
        firstname = request.form.get('first-name')
        lastname = request.form.get('last-name')
        job_title = request.form.get('job-title')
        city = request.form.get('city')
        phone = request.form.get('phone')
        address = request.form.get('address')
        postal_code = request.form.get('postal-code')
        storage.update_user_profile(id=user_id, job_title=job_title, city=city)
    return render_template("main/informations.html", user=curr_user)


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
