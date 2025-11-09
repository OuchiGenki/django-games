# Genki's Portfolio — django-games

Django で作成したミニゲーム集（ポートフォリオ）です。\
学習・スキル証明・作品公開を目的としており、今後も継続的にゲームを追加していく予定です。

現在実装済みのゲーム:

-   Othello（オセロ）
<img width="1440" height="790" alt="Image" src="https://github.com/user-attachments/assets/b38f8cb9-2ea1-4207-8202-9b452ec22c5a" />
-   Hit & Blow

------------------------------------------------------------------------

## 概要

- 言語: Python 3.13
- フレームワーク: Django
- DB: SQLite（開発用）
- フロント: Bootstrap（テンプレートで利用）
- テスト: pytest / Django の test runner

現在の主要実装ゲーム:

- Othello（オセロ）
- Hit & Blow

------------------------------------------------------------------------

## ローカルでの簡易セットアップ

1. リポジトリをクローンして作業ディレクトリへ移動
2. 仮想環境を作成・有効化
3. 依存パッケージをインストール
4. マイグレーション実行後、開発サーバを起動

コマンド例（zsh）:

```zsh
git clone https://github.com/OuchiGenki/django-games.git
cd django-games
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

ブラウザで `http://127.0.0.1:8000` にアクセスしてください。

------------------------------------------------------------------------

## 実装のポイント（Othello）

- コアロジックの分離
  - 盤面操作やゲームルール（盤面初期化、合法手判定、石の反転、ターン管理、パス判定、勝敗判定など）は `othello/game_logic.py` にまとめています。

- 盤面の永続化（JSONField を使用）
  - 盤面データは `othello.models.Game` の `board` フィールドに `JSONField` を用いて保存しています。
  - 表示時はモデルから読み出して `game_logic` の関数で解析・判定を行います。

- 認証機能について
  - Django の標準認証を使用し、ログイン済みユーザーごとにゲームを作成・保存できます。これによりユーザーは中断したゲームを再開できます。

- 開発ブランチ運用
  - 機能単位でブランチを切り、プルリクエスト（PR）でレビューしてから main（または develop）へマージしています。
  - 例: `feature/othello`（オセロ用の親ブランチ）、`feature/logic`（コアロジック）、`feature/views`（ビューとテンプレート）

------------------------------------------------------------------------

## テスト

ユニットテストは pytest または Django のテストランナーで実行できます。

```zsh
python3 -m pytest
```

テストは主に `othello/` のロジック関数を対象に作成しています。

------------------------------------------------------------------------

## 今後の予定（TODO）

- 追加ゲームの実装
- UI/アクセシビリティの改善
- 部分更新（AJAX）による操作性向上
- デプロイ手順の整備

------------------------------------------------------------------------

## 連絡先

- GitHub: https://github.com/OuchiGenki
- Email: ouchigenki2025@gmail.com

------------------------------------------------------------------------
