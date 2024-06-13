import flet as ft
from flet_route import Routing, path
from Views.Home import Home
from Views.Login import Login


def main(page: ft.Page):
    page.bgcolor = "#FFFFFF"
    app_routes = [
        path(
            url="/",
            clear=True,
            view=Home,
        ),
        path(url="/next_view/:my_id", clear=False, view=Login),
    ]

    Routing(
        page=page,
        app_routes=app_routes,
    )
    page.go(page.route)


ft.app(target=main)
