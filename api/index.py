from flask import Flask, jsonify, url_for


app = Flask(__name__)


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text