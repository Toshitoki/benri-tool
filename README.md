# Benri-Searcher
検索したいものをテキストボックスに入力することで、任意のWebページで検索することができます

---

# URLの登録方法
SearchPages.jsonファイルにURLを記入することで、検索するページを追加することができます。

(例)
google と Aucfree で検索する場合、以下のように SearchPages.json を編集します：

```json:SearchPages.json
"link1": {
        "url": "https://www.google.com/search?q={query}"
    },

"link2": {
    "url": "https://www.aucfree.com/search?from={last_year}-{month}&q={query}&to={year}-{month}"
    }
```
linkの後の数字の部分は他と被らない一意の数字又は文字を入力してください。

他に検索したいページがある場合は、{ }のあとに , (コンマ)をつけて記入してください。

---

# 利用できる引数
このソフトでは、検索に必要な変数をいくつか指定することができます。

### 1.{query}
検索バーに入力した文字列を利用することができます。

### 2.{year}
現在の年の値を利用することができます。

### 3.{month}
現在の月の値を利用することができます。

### 4.{date}
現在の日付の値を利用することができます。

### 5.{last_year}
去年の年の値を利用することができます。