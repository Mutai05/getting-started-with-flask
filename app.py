from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the Homepage
@app.route('/')
def index():
    return render_template("index.html")

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)