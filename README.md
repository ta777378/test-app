# test-app（タスク管理アプリ）

## 📌 プロジェクト概要

学習用に作るフルスタックWebアプリ。  
Python（Flask） + TypeScript（React）で構成。DockerやAWSなどの技術も扱う予定。

---

## 🛠 技術スタック

- バックエンド：Python + Flask
- フロントエンド：React + TypeScript + Vite
- DB：SQLite（→ PostgreSQL）
- インフラ：Docker / Kubernetes（予定） / AWS（予定）

---

## 📂 ディレクトリ構成
test-app/ 
├── backend/ # Flask アプリ（API） 
├── frontend/ # React アプリ（UI） 
└── README.md # このマニュアル

## 🚀 セットアップ方法

### ✅ 1. 前提環境（WSL/Ubuntu内で作業）

- Python 3.x
- Node.js（npm）
- Git
- Flask / React は手順で自動インストールされます

---

### ✅ 2. 開発環境の構築手順

### ✅ Flask（バックエンド）

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install Flask
python app.py
###アクセス：http://localhost:5000

### ✅ React（フロントエンド）
```bash
cd frontend
npm install
npm run dev

###アクセス：http://localhost:5173