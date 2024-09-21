import os
from os import abort
from re import search

from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from sqlalchemy.sql.functions import current_user
from werkzeug.utils import secure_filename

app = Flask(__name__)
from models import storage

app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


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
    if session.get('user_id') is None:
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    curr_user = storage.get_user_by_id(user_id)

    if request.method == 'POST':
        # Get other form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        job_title = request.form.get('job-title')
        city = request.form.get('city')
        bio = request.form.get("bio")
        small_bio = request.form.get("small_bio")
        github_url = request.form.get("github_url")
        facebook_url = request.form.get("facebook_url")
        linkedln = request.form.get("linkedln")
        stackoverflow = request.form.get("stackoverflow")
        medium_url = request.form.get("medium_url")

        # Handle the file upload
        file = request.files['file-upload']

        # Check if the file is allowed (is a valid image)
        if file and allowed_file(file.filename):
            # Ensure filename is secure
            filename = secure_filename(file.filename)

            # Save the file in the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # You can save the filename or file path to the user's profile
            storage.post_profile_pic(id=user_id, profile_pic=filename)

        # Update user information
        storage.update_user_profile(id=user_id, job_title=job_title, city=city, firstname=firstname,
                                    lastname=lastname, bio=bio, small_bio=small_bio, github_url=github_url,
                                    facebook_url=facebook_url, linkedln=linkedln, stackoverflow=stackoverflow,
                                    medium_url=medium_url)

        return redirect(url_for('home'))

    return render_template("main/informations.html", user=curr_user, user_id=user_id)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/dashboard')
def dashboard():
    return render_template("main/dashboard.html")


@app.route("/messages")
def messages():
    return render_template("main/messages.html")


@app.route("/home", methods=['GET', 'POST'])
def home():
    if session.get('user_id'):
        curr_user = storage.get_user_by_id(session['user_id'])
        if request.method == 'POST':
            search = request.form['search'].split()
            if search:
                return redirect(url_for('feed', search=search, user=curr_user))
            else:
                return redirect(url_for('home', user=curr_user))
    else:
        return redirect(url_for('login'))
    return render_template("main/home.html")


@app.route("/feed", methods=['GET', 'POST'])
def feed():
    if session.get('user_id') is None:
        return redirect(url_for('login'))
    else:
        curr_user = storage.get_user_by_id(session['user_id'])
    users = []
    if request.method == "POST":
        search_input = request.form.get("search").strip()
        if search_input:
            users = storage.get_users_by_job_title(search_input)
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
                return redirect(url_for('home', user=current_user))
    return render_template("main/feed.html", users=users, user=curr_user)


@app.route('/userpage/<username>')
def userpage(username):
    user = storage.get_user_by_username(username)
    print(user)
    if user is None:
        return redirect(url_for('not_found'))
    return render_template("main/user_page.html", user=user)


@app.route('/404')
def not_found():
    return """ <p> user not found </p> """


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    # Handle user exiting (log out the user, store activity, etc.)
    if 'user_id' in session:
        user_id = session['user_id']
        # Do something, such as logging the exit or removing user session
        print(f"User {user_id} has left the website.")
        session.pop('user_id', None)
        return redirect(url_for('login'))
    return redirect(url_for('login'))

