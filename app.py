from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

app = Flask(__name__)
# Configure the Flask app to connect to a SQLite database named affirmations.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///affirmations.db'
db = SQLAlchemy(app)

# Flask-Login configuration
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from models import *

@app.route('/')
def home():
    # Render the home page template when the root URL is accessed
    return render_template('home.html')

@app.route('/select_categories', methods=['GET', 'POST'])
def select_categories():
    if request.method == 'POST':
        # Placeholder for processing selected categories after form submission
        return redirect(url_for('home'))
    # Render the category selection page template
    return render_template('select_categories.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not User.query.filter_by(email=email).first():
            user = User(email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('home'))
        else:
            # Here, you might want to add a flash message or some error handling
            pass
    return render_template('login.html')


if __name__ == '__main__':
    db.create_all()  # Create the database tables based on the models at startup
    app.run(debug=True)  # Run the Flask app in debug mode
