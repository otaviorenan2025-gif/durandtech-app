import flet as ft

URL = "https://www.durandtechsysten.com.br"

def main(page: ft.Page):
    page.title = "DurandTech Systen"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0f172a"
    page.padding = 0
    page.window_width = 400
    page.window_height = 800

    webview = ft.WebView(
        url=URL,
        expand=True,
        enable_javascript=True,
    )

    page.add(webview)

ft.app(target=main)
