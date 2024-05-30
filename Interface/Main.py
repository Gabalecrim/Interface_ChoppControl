import flet as ft
from flet_route import *
from Views import Home
from Views import Login
from Views import Page1

def main(page: ft.Page):

    app_routes = [
        path(url ="/", clear=True, view=Home),
        path(url="/login", clear=True, view=Login),
        path(url="/page1", clear=True, view=Page1)
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

ft.app(target=main)
