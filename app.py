from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Get the directory where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_index():
    # Serve index.html from the same directory as this script
    return send_from_directory(base_dir, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
