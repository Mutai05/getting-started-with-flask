from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the Homepage
@app.route('/')
def index():
    return "Hello World!"

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)