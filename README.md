# Genki's Portfolio — django-games

Django で作成したミニゲーム集（ポートフォリオ）です。  
学習・スキル証明・作品公開を目的としており、今後も継続的にゲームを追加していく予定です。

現在実装済みのゲーム:

- **Gomoku（五目並べ） ← New!**
  <img width="1440" height="811" alt="Image" src="https://github.com/user-attachments/assets/fa2ad2cc-8edb-41d9-8bf2-3519ad0a71ba" />
  - AJAX（Fetch API）で盤面を部分更新するインタラクティブ仕様

- Othello（オセロ)
  - コアロジックを `gomoku/game_logic.py` に分離
  - 盤面の永続化
  <img width="1440" height="790" alt="Image" src="https://github.com/user-attachments/assets/b38f8cb9-2ea1-4207-8202-9b452ec22c5a" />

- Hit & Blow
  - チュートリアルとして作成したミニゲームです

---

## 概要

- 言語: Python 3.13  
- フレームワーク: Django  
- DB: SQLite（開発用）  
- フロント（抜粋）: Bootstrap / Fetch API
- テスト: pytest / Django テストランナー  

現在の主要実装ゲーム:

- Othello（オセロ）
- Hit & Blow
- Gomoku（五目並べ）

---

## ローカルでの簡易セットアップ

1. リポジトリをクローン
2. 仮想環境を作成・有効化
3. 依存パッケージをインストール
4. マイグレーション実行
5. 開発サーバを起動

例（zsh）:

```zsh
git clone https://github.com/OuchiGenki/django-games.git
cd django-games
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

ブラウザで http://127.0.0.1:8000 にアクセス。

---

## 実装のポイント（Gomoku / 五目並べ） 🎉 New

- Fetch API を用いた AJAX 実装
  - ボタン（石を置く位置）を押すと  
    → Fetch APIが更新用URLを叩く
    → view 側で盤面を更新  
    → 最新盤面を JSON で返却  
    → JS 側で盤面を再描写  
  - ページリロードなしで高速に更新することができた！！

- 盤面描画は JavaScript で動的に更新  
  テンプレート初期表示後はすべて JS の `updateBoard()` で DOM 更新。ゲームの状態管理がしやすく、レスポンスが軽い設計。

- 盤面データは `JSONField` で永続化  
  Django 側で盤面を完全管理 → ブラウザは表示のみ。

- コアロジックを `gomoku/game_logic.py` に分離  
---

## 実装のポイント（Othello）

- コアロジックの分離  
  初期化・合法手判定・反転・ターン切替などを `othello/game_logic.py` に集約。  

- 盤面の永続化  
  `JSONField` を用いて盤面を `othello.models.Game` に保存。表示時に `game_logic` で解析。  

- ユーザー別にゲームを保存  
  Django 認証と紐づいたゲーム管理。  

- ブランチ運用  
  `feature/othello` → `feature/logic` → `feature/views` のように小分けで PR。

---


## テスト

```zsh
python3 -m pytest
```

主に以下を対象にユニットテストを作成：

- ゲームロジック

---

## 今後の予定（TODO）

- 新規ゲーム追加
- UI/UX 改善（レスポンシブ、アニメーション）  
- 各ゲームの API 化（部分更新の高速化）  
- デプロイ手順整備

---

## 連絡先

- GitHub: https://github.com/OuchiGenki  
- Email: ouchigenki2025@gmail.com

---
