import flet as ft
import webbrowser
import time
import json
import os

# jsonファイルのパス
json_file_path = './SearchPages.json'

# jsonファイルを読み込む
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_open:
        json_load = json.load(json_open)
        print("jsonファイルを読み込みました")
else:
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
    with open(json_file_path, 'w') as json_file:
        json.dump(default_data, json_file, indent=4)
    json_load = default_data
    print("jsonファイルを作成しました")

def main(page: ft.Page):
    page.title = "EZ Searcher"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    tb1 = ft.TextField(label="Enter product name/Model")
    search_button = ft.ElevatedButton(text="Search", on_click=lambda e: search_test(tb1.value))
    result_container = ft.Column()

    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    date = time.localtime().tm_mday
    last_year = year - 1

    def search_test(query):
        result_container.controls.clear()
        # jsonのURLの個数分繰り返す
        for v in json_load.values():
            url = v['url'].format(query=query, year=year, month=month, last_year=last_year, date=date)
            link = ft.TextButton(text=url, on_click=lambda e, url=url: webbrowser.open(url))
            result_container.controls.append(link)
        page.update()

    page.add(tb1)
    page.add(search_button)
    page.add(result_container)

ft.app(main)