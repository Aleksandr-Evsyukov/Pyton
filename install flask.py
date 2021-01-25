from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/add/<int:x>/<int:y>')
def show_post(x, y):
    return str(x + y)