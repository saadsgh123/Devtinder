from re import search

from flask import Flask, render_template, request, redirect, url_for, flash

from models import storage

app = Flask(__name__)
app.secret_key = 'your_super_secret_key' #decoy key

#decoy data for testting
user_data = {
    'user1': {
        'id' : 'user1',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'Qp5pG@example.com',
        'job_title': 'FullStack',
        'phone_number': '123-456-7890',
        'address': '123 Main St',
        'postal_code': '12345',
        'city': 'Anytown',
        'portfolio': 'https://example.com'
    }
}

@app.route('/')
def landing_page():
    return render_template("auth/landing_page.html", title='Dev Tinder - Find Your Ideal Tech Talent')


@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/register')
def register():
    return render_template("auth/register.html")

@app.route('/information', methods=['GET', 'POST'])
def information():
    #user_id = session.get('user_id', 'user1')  # Simulate user login
    user_id = 'user2'

    if request.method == 'POST':
        user_info = {
            'id': user_id,
            'first_name': request.form.get('first-name'),
            'last_name': request.form.get('last-name'),
            'email': request.form.get('email'),
            'job_title': request.form.get('job-title'),
            'phone_number': request.form.get('phone-number'),
            'address': request.form.get('address'),
            'postal_code': request.form.get('postal-code'),
            'city': request.form.get('city'),
            'portfolio': request.form.get('portfolio')
        }
        

        user_data[user_id] = user_info

        return redirect(url_for('information'))

    if user_id in user_data:
        user_info = user_data[user_id] 
    else:

        user_info = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'job_title': '',
            'phone_number': '',
            'address': '',
            'postal_code': '',
            'city': '',
            'portfolio': ''
        }

    # Render the form with user information (blank or pre-filled)
    return render_template('main/informations.html', user_info=user_info)


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


from flask import jsonify

@app.route("/feed", methods=['GET', 'POST'])
def feed():
    users = []
    
    # Handle POST requests (search via form submission)
    if request.method == "POST":
        search = request.form.get("search").strip()
        if search:
            users = storage.get_users_by_job_title(search)
            if not users:
                flash("No users found", category="error-message")
        else:
            flash("Search field cannot be empty!", "error-message")

    # Handle AJAX GET requests (filtering without page reload)
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url_search = request.args.get("search")
        experience = request.args.get("experience")
        location = request.args.get("location")

        # Filter logic based on received parameters
        if url_search or experience or location:
            users = storage.get_filtered_users(url_search, experience, location)
        else:
            users = storage.get_all_users()

        # Construct a JSON response for the filtered users
        users_json = [
            {
                'username': user.username,
                'job_title': user.job_title,
                'freelancer': user.freelancer,
                'technologies': user.technologies,
                'description': user.description
            } for user in users
        ]
        return jsonify({'users': users_json})

    # Fallback for normal GET requests (without AJAX)
    elif request.method == "GET":
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

