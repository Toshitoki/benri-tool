import flet as ft
import webbrowser
import time
import json

# jsonファイルを読み込む
json_open = open("SearchPages.json", "r")
json_load = json.load(json_open)


def main(page: ft.Page):
    page.title = "EZ Searcher"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    tb1 = ft.TextField(label="Enter product name/Model")
    search_button = ft.ElevatedButton(text="Search", on_click=lambda e: (search_test(tb1.value)))

    year = time.localtime().tm_year
    month = time.localtime().tm_mon

    def search_test(query):
        #jsonで去年を指定できるようにする
        last_year = year - 1

        #jsonのURLの個数分繰り返す
        for v in json_load.values():
            url = v['url'].format(query=query, year=year, month=month,last_year=last_year)
            webbrowser.open(url)

    page.add(tb1)
    page.add(search_button)
ft.app(main)