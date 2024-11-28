import flet as ft
print("hello world")

import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    tb1 = ft.TextField(label="Enter product name/Model")

    page.add(tb1)

ft.app(main)