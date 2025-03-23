# backend/app.py
from flask import Flask
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)

# DB設定（SQLite使用）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mytask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # 初期化時にテーブル作成

@app.route("/api/hello")
def hello():
    return "Hello from Flask API!"
