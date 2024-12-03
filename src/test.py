import tkinter as tk
from tkinter import messagebox
import time
import pyperclip
import webbrowser
import sqlite3

# データベースの設定
conn = sqlite3.connect('URLs.db')
c = conn.cursor()

# デフォルトのURLデータをデータベースから読み込む関数
def load_default_data():
    data = {}
    for row in c.execute("SELECT name, url FROM urls"):
        data[row[0]] = {"url": row[1]}
    return data

default_data = load_default_data()

def search_test(query):
    # 結果フレーム内の既存のウィジェットを全て削除
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    # 現在の年、月、前年を取得
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    last_year = year - 1

    # デフォルトのURLデータの個数分繰り返す
    for v in default_data.values():
        # URLをフォーマットして生成
        url = v["url"].format(query=query, year=year, month=month, last_year=last_year)
        # URLを表示するラベルを作成
        link_label = tk.Label(result_frame, text=url, fg="blue", cursor="hand2")
        link_label.pack()
        
        # URLをコピーするボタンを作成
        copy_button = tk.Button(result_frame, text="Copy", command=lambda url=url: pyperclip.copy(url))
        copy_button.pack()
        
        # ブラウザでURLを開く
        webbrowser.open(url)

# メインウィンドウの設定
root = tk.Tk()
root.title("So-ba Searcher")

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

# データベース接続を閉じる
conn.close()