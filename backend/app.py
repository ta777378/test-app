from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def api_hello():
    return jsonify(message="Hello from Flask API!")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', use_reloader=False)
