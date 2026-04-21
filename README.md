# electron-sqlite-practice

Electron（フロントエンド）+ FastAPI（バックエンド）+ SQLite を使用したシンプルなデスクトップ PoC です。

## プロジェクト構成

- backend/: FastAPI サーバーと SQLite ロジック
- frontend/: Electron アプリ UI

## 機能

- Electron UI からタスクを FastAPI に送信
- タスクを SQLite（tasks.db）に保存
- SQLite からタスクを読み込んで UI に表示

## 必要な環境

- Python 3.10+
- Node.js 18+
- npm

## セットアップ

### 1. バックエンドのセットアップ

backend フォルダから：

```bash
cd backend
pip install -r requirements.txt
```

### 2. フロントエンドのセットアップ

frontend フォルダから：

```bash
cd frontend
npm install electron --save-dev
```

## 実行方法

### 1. バックエンドを起動

backend フォルダから：

```bash
uvicorn main:app --reload
```

サーバーは以下で実行されます：

- http://127.0.0.1:8000

### 2. Electron アプリを起動

新しいターミナルを開き、frontend フォルダから：

```bash
npx electron .
```

## API エンドポイント

- POST /add_task
  - body: {"content": "タスク内容"}
- GET /get_tasks
  - response: {"tasks": ["タスク1", "タスク2"]}

## 注記

- SQLite ファイル tasks.db は backend フォルダに作成されます。
- これは PoC 構成です。Electron は nodeIntegration を有効化し、contextIsolation を無効化しています（簡略化のため）。
