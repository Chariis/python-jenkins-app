from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from CI/CD with Jenkins! My name is charis"
