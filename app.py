from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
data = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data', methods=['POST'])
def receive_data():
    content = request.json
    content['timestamp'] = time.time()
    data.append(content)
    # Keep only last 20 entries
    if len(data) > 20:
        data.pop(0)
    return jsonify({"status": "received"})

@app.route('/data', methods=['GET'])
def send_data():
    return jsonify(data)

if __name__ == '__main__':
    import time
    app.run(debug=True)
