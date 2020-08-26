# HackU API設計

## メモ
* 全体の時間（３０分）に対して１分刻みは長いのでは？
    * もう少し短いスパンでいい、もしくは全体の時間を長くした方がいいのでは

## 要件定義
### ユーザー関連

1. ユーザーを登録する
2. ユーザー一覧の取得
3. ユーザーのログイン

### コンテスト関連
#### コンテスト
+ 開催期間
+ 順位表
+ 値動きのデータ

1. コンテストの追加
2. コンテストへの参加
3. 順位表/株価のデータを渡す
4. 株の売買


## アクセスポイント
`/` [GET]
### 概要
アクセス確認用
### 送るjson
### 返ってくるjson
```json
{
  "message": "unnko"
}
```

---

`/user/add` [POST]
### 概要
ユーザーを追加する
### 送るjson
```json
{
  "username": "nanigasi_san",
  "password_hash": "1a1dc91c907325c69271ddf0c944bc72"
}
```
### 返ってくるjson
200
```json
{
  "message": "add user nanigasi_san.",
}
```

404
```json
{
  "message": "user nanigasi_san is exists."
}
```

---

`/user/list` [GET]
### 概要
username一覧
### 送るjson
### 返ってくるjson
```json
[
  "nanigasi_san",
  "hureki"
]
```

---

`/user/login` [POST]
### 概要
password_hashのチェック
### 送るjson
```json
{
  "username": "nanigasi_san",
  "password_hash": "1a1dc91c907325c69271ddf0c944bc72"
}
```
### 返ってくるjson
```json
{
  "check": true
}
```
