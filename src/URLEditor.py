#検索するためのURLを管理するソフト

import tkinter as tk
from tkinter import messagebox
import sqlite3
import pyperclip
import webbrowser

# データベースの設定
conn = sqlite3.connect('./URLs.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (id INTEGER PRIMARY KEY, name TEXT, url TEXT)''')
conn.commit()

# URLを追加する関数
def add_url():
    name = name_entry.get()
    url = url_entry.get()
    if name and url:
        c.execute("INSERT INTO urls (name, url) VALUES (?, ?)", (name, url))
        conn.commit()
        name_entry.delete(0, tk.END)
        url_entry.delete(0, tk.END)
        load_urls()
    else:
        messagebox.showwarning("入力エラー", "名前とURLを入力してください")

# URLを削除する関数
def delete_url():
    selected_item = url_listbox.curselection()
    if selected_item:
        confirm = messagebox.askyesno("確認", "本当に削除しますか？")
        if confirm:
            url_id = url_listbox.get(selected_item).split()[0]
            c.execute("DELETE FROM urls WHERE id=?", (url_id,))
            conn.commit()
            load_urls()
    else:
        messagebox.showwarning("選択エラー", "削除するURLを選択してください")


# URLを読み込む関数
def load_urls():
    url_listbox.delete(0, tk.END)
    for row in c.execute("SELECT * FROM urls"):
        url_listbox.insert(tk.END, f"{row[0]} {row[1]}: {row[2]}")

# URLを検索する関数
def search_test(query):
    for widget in result_frame.winfo_children():
        widget.destroy()
    for row in c.execute("SELECT * FROM urls"):
        url = row[2].format(query=query)
        link_label = tk.Label(result_frame, text=url, fg="blue", cursor="hand2")
        link_label.pack()
        copy_button = tk.Button(result_frame, text="Copy", command=lambda url=url: pyperclip.copy(url))
        copy_button.pack()
        webbrowser.open(url)

# メインウィンドウの設定
root = tk.Tk()
root.title("URL Manager")
root.geometry("600x380")

# URL追加用の入力フィールド
tk.Label(root, text="ページ名").pack(fill=tk.X, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(fill=tk.X, padx=10, pady=5)
tk.Label(root, text="URL").pack(fill=tk.X, padx=10, pady=5)
url_entry = tk.Entry(root)
url_entry.pack(fill=tk.X, padx=10, pady=5)
tk.Button(root, text="URLを追加", command=add_url).pack(fill=tk.X, padx=10, pady=5)

# URLリスト表示用のリストボックス
url_listbox = tk.Listbox(root)
url_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
tk.Button(root, text="URLを削除", command=delete_url).pack(fill=tk.X, padx=10, pady=5)

# 結果表示用フレーム
result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)


# URLを読み込む
load_urls()

# メインループの開始
root.mainloop()

# データベース接続を閉じる
conn.close()