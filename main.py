from re import search

from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy.sql.functions import current_user

from models import storage

app = Flask(__name__)
from models import storage

app.secret_key = 'your_secret_key'


@app.route('/')
def landing_page():
    if session.get('user_id'):
        return redirect(url_for('home'))
    return render_template("auth/landing_page.html", title='Dev Tinder - Find Your Ideal Tech Talent')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = storage.get_user_by_email(email)
        if user is not None:
            if user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password', 'error')
        else:
            flash('Invalid email or password', 'error')
    return render_template("auth/login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password == confirm_password:
            new_user = storage.create_user_profile(username=username, email=email, password=password)
            session['user_id'] = new_user.id
            return redirect(url_for('informations'))
    return render_template("auth/register.html")


@app.route('/informations/', methods=['GET', 'POST'])
def informations():
    user_id = session.get('user_id')
    curr_user = storage.get_user_by_id(user_id)
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        job_title = request.form.get('job-title')
        city = request.form.get('city')
        bio = request.form.get("bio")
        small_bio = request.form.get("small_bio")
        github_url = request.form.get("small_bio")
        facebook_url = request.form.get("facebook_url")
        linkedln = request.form.get("linkedln")
        stackoverflow = request.form.get("stackoverflow")
        medium_url = request.form.get("medium_url")
        storage.update_user_profile(id=user_id, job_title=job_title, city=city, firstname=firstname,
                                    lastname=lastname, bio=bio, small_bio=small_bio, github_url=github_url,
                                    facebook_url=facebook_url, linkedln=linkedln,
                                    stackoverflow=stackoverflow, medium_url=medium_url)
        return redirect(url_for('home'))
    return render_template("main/informations.html", user=curr_user, user_id=user_id)


@app.route('/dashboard')
def dashboard():
    return render_template("main/dashboard.html")


@app.route("/messages")
def messages():
    return render_template("main/messages.html")


@app.route("/home", methods=['GET', 'POST'])
def home():
    if session.get('user_id'):
        print(session.get('user_id'))
        if request.method == 'POST':
            search = request.form['search'].split()
            if search:
                return redirect(url_for('feed', search=search))
            else:
                return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
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


@app.route('/userpage/<username>/<user_id>')
def userpage(username, user_id):
    user = storage.get_user_by_id(user_id)
    if user is None:
        return render_template("404.html")  # or redirect to a custom 404 page if needed
    return render_template("main/user_page.html", user=user)


@app.route('/404')
def not_found():
    return """ <p> user not found </p>"""


@app.route('/user-exit', methods=['POST'])
def user_exit():
    # Handle user exiting (log out the user, store activity, etc.)
    if 'user_id' in session:
        user_id = session['user_id']
        # Do something, such as logging the exit or removing user session
        print(f"User {user_id} has left the website.")
        session.pop('user_id', None)  # Clear session if needed
    return '', 204  # Return no content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
