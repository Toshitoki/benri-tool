import flet as ft
import webbrowser
import time
def main(page: ft.Page):
    page.title = "EZ Searcher"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    tb1 = ft.TextField(label="Enter product name/Model")
    search_button = ft.ElevatedButton(text="Search", on_click=lambda e: (search_google(tb1.value), search_aucfree(tb1.value)))

    year = time.localtime().tm_year
    month = time.localtime().tm_mon

    def search_google(query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    def search_aucfree(query):
        url = f"https://www.aucfree.com/search?from={year-1}-{month}&q={query}&to={year}-{month}"
        webbrowser.open(url)

    page.add(tb1)
    page.add(search_button)

ft.app(main)