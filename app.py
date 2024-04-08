from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the Flask app to connect to a SQLite database named affirmations.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///affirmations.db'
db = SQLAlchemy(app)

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

if __name__ == '__main__':
    db.create_all()  # Create the database tables based on the models at startup
    app.run(debug=True)  # Run the Flask app in debug mode
