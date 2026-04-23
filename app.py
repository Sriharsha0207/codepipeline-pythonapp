from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    username = os.environ.get("DB_USERNAME", "Not Set")
    return f"Flask App Running 🚀 | User: {username}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
