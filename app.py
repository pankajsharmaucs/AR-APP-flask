from flask import Flask, render_template
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Get the PORT environment variable from Render
    port = int(os.environ.get("PORT", 5000))
    # Set the host to '0.0.0.0' for production
    app.run(host='0.0.0.0', port=port)
