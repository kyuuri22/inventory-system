# 📦 Inventory System

Pythonで作成した在庫管理システムです。
CLIとFlask Web版の両方に対応しています。

## 動作環境

- Python 3.8 以上
- Flask（Web版のみ）

## セットアップ

```bash
git clone https://github.com/shunsukekato22/inventory-system.git
cd inventory-system
pip install flask
```

## デモ

https://inventory-system-4evn.onrender.com

## 起動方法（ローカル）

**Web版（Flask）**
```bash
python app.py
```
起動後、ブラウザで `http://127.0.0.1:5000` を開いてください。

**CLI版**
```bash
python main.py
```

## 機能一覧

### Web版

| 機能 | 説明 |
|------|------|
| 商品登録 | 新しい商品を在庫リストに追加します |
| 入庫 | 指定した商品の在庫数を増やします |
| 出庫 | 指定した商品の在庫数を減らします |
| 商品名変更 | 登録済みの商品名を変更します |
| 商品削除 | 商品を在庫リストから削除します |
| 在庫一覧 | 現在の全在庫を表示します（在庫0は赤字） |
| 在庫数直接編集 | 一覧テーブルから在庫数を直接更新できます |

### CLI版

起動するとメニューが表示されます。

```
1.商品登録
2.入庫
3.出庫
4.一覧表示
5.商品削除
6.終了
番号を選んでください:
```

操作のたびに inventory.json へ自動保存されます。

## ファイル構成

```
inventory-system/
├── main.py               # InventoryManagerクラス（CLI・Web共通）
├── app.py                # FlaskアプリケーションのWebサーバー
├── templates/
│   └── index.html        # Web版のUI
├── inventory.json        # 在庫データ（自動生成）
└── README.md
```

## 技術的なポイント

- InventoryManager クラスで在庫データと操作を一元管理
- _load() / _save() で JSON ファイルへの永続化を実装
- _input_number() で数値入力の共通バリデーション処理を共通化
- 不正入力・存在しない商品・在庫不足などの例外処理を実装済み

## 今後の予定

- [x] Web化（Flask）
- [x] 商品削除機能
- [ ] 在庫数の下限アラート
