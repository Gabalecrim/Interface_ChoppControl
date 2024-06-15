import flet as ft
from flet_route import Routing, path
from Views.Home import Home
from Views.Login import Login
from Views.Configs import Configs


def main(page: ft.Page):
    # page.window_center()
    page.window_bgcolor = "#192026"
    page.title = "Chopp Control"
    page.window_min_height = 700
    page.window_min_width = 1000

    app_routes = [
        path(
            url="/",
            clear=True,
            view=Home,
        ),
        path(url="/next_view/:my_id", clear=False, view=Login),
        path(url="/configs", clear=False, view=Configs),
    ]

    Routing(
        page=page,
        app_routes=app_routes,
    )
    page.go(page.route)


ft.app(target=main)
