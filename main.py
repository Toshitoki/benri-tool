import tkinter as tk
from tkinter import messagebox
import time
import json
import pyperclip

# jsonファイルを読み込む
try:
    with open('./SearchPages.json', 'r') as json_open:
        json_load = json.load(json_open)
        print("jsonファイルを読み込みました")
except FileNotFoundError:
    # ファイルが存在しない場合、新しいファイルを作成
    default_data = {
        "link1": {
            "url": "https://www.google.com/search?q={query}"
        },
        "link2": {
            "url": "https://www.aucfree.com/search?from={last_year}-{month}&q={query}&to={year}-{month}"
        },
        "link3": {
            "url": "https://jp.mercari.com/search?keyword={query}"
        }
    }
    # 新しいjsonファイルを作成し、デフォルトデータを書き込む
    with open('SearchPages.json', 'w') as json_file:
        json.dump(default_data, json_file, indent=4)
    json_load = default_data
    print("jsonファイルを作成しました")

def search_test(query):
    # 結果フレーム内の既存のウィジェットを全て削除
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    # 現在の年、月、前年を取得
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    last_year = year - 1

    # jsonのURLの個数分繰り返す
    for v in json_load.values():
        # URLをフォーマットして生成
        url = v["url"].format(query=query, year=year, month=month, last_year=last_year)
        # URLを表示するラベルを作成
        link_label = tk.Label(result_frame, text=url, fg="blue", cursor="hand2")
        link_label.pack()
        
        # URLをコピーするボタンを作成
        #copy_button = tk.Button(result_frame, text="Copy", command=lambda url=url: pyperclip.copy(url))
        #copy_button.pack()

# メインウィンドウの設定
root = tk.Tk()
root.title("EZ Searcher")

# 入力フィールド
label = tk.Label(root, text="Enter product name/Model")
label.pack()
tb1 = tk.Entry(root)
tb1.pack()

# 検索ボタン
search_button = tk.Button(root, text="Search", command=lambda: search_test(tb1.get()))
search_button.pack()

# 結果表示用フレーム
result_frame = tk.Frame(root)
result_frame.pack()

# メインループの開始
root.mainloop()