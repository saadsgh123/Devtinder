#!/usr/bin/python3
from flask import Flask, render_template, flash, redirect, url_for, request, flash
from form import RegisterForm, LoginForm
from models import storage

app = Flask(__name__)

app.config['SECRET_KEY']='e6148d38d0678be929e2242658219bb2a54341d6f79187de719c5f1a5bee28a5'
app.config['WTF_CSRF_ENABLED'] = True

user = {
        'profile_image': 'static/images/my-image.jpeg',
        'name': 'Badr Bouzagui',
        'skillls': ['Python', 'SQL', 'JavaScript', 'MySQL', 'CSS3', 'HTML5', 'C'],
        'skills': [
            {
                'python': '../../static/images/python.png',
                'sql': '../../static/images/sql-server.png',
                'javascript': '../../static/images/java-script.png',
                'mysql': '../../static/images/mysql.png',
                'css': '../../static/images/css.png',
                'html': '../../static/images/html.png',
                'c': '../../static/images/letter-c.png'
            }
        ],
        'specialization': 'Full Stack Web Developer',
        'github': 'https://github.com/Bouzagui',
        'linkedin': 'https://www.linkedin.com/in/badr-bouzagui-23aa41265',
        'twitter': 'https://twitter.com/BBouzagui',
        'educations': [
            {
                'institution': 'ALX Software Engineering University online',
                'program': 'Holberton School',
                'date': 'August 2023 - present',
                'imageeducation': '../../static/images/school.png'
            },
        ],
        'projects': [
            {
                'title': 'AirBnb Clone',
                'imageproject': '../../static/images/airbnb.png',
                'description': 'This is an AirBnb clone made"\n" with Python, Flask, and MySQL',
                'image': 'images/airbnb.png'
            },
            {
                'title': 'Simple Shell',
                'imageproject': '../../static/images/simple-shell.png',
                'description': 'This is a simple shell made with C.',
                'image': 'images/simple-shell.png'
            }
        ]
    }

@app.route('/')
@app.route('/landing_page')
def landing_page():
    return render_template("auth/landing_page.html")

@app.route("/profil")
def profil():
    return render_template('main/profil_account.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print("Form submitted")
        if form.email.data == 'badrbouzagui@gmail.com' and form.password.data == 'Badr@1998':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))  # Redirect to home on successful login
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    # else:
    #     print("Form validation failed:", form.errors)

    return render_template("auth/login.html", form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
       flash(f"Account created successfully for {form.fname.data}, {form.lname.data}", 'success')
       return redirect(url_for('home'))
    return render_template("auth/register.html", form=form)

@app.route('/informations', methods=['POST'])
def informations():
    if request.method == 'POST':
        flash(f"Account created successfully for {request.form['fname']} {request.form['lname']}", 'success')
        return redirect(url_for('home'))
    return render_template("main/home.html")

@app.route('/dashboard')
def dashboard():
    return render_template("main/dashboard.html")


@app.route("/messages")
def messages():
    return render_template("main/messages.html")


@app.route("/home")
def home():
    # if request.method == 'POST':
    #     return redirect(url_for('home'))
    return render_template("main/home.html", user=user)


@app.route("/feed")
def feed():
    try:
        users = storage.all().values()
        return render_template("main/feed.html", users=list(users))
    except Exception as e:
        flash(f"Error loading feed: {e}", 'danger')
        return redirect(url_for('dashboard'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
