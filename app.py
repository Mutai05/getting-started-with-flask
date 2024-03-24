from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)
app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///test.db'
db = SQLAlchemy(app)




# Define a route for the Homepage
@app.route('/')
def index():
    return render_template("index.html")

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)