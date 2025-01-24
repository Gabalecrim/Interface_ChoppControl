import flet as ft
from flet_route import Routing, path
from Views.Home import Home
from Views.Login import Login
from Views.Configs import Configs
import threading
import time
import Allan_utils


def main(page: ft.Page):
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


def Setpoint():

    while True:
        time.sleep(0.1)
        Speed = Allan_utils.espUtils.sendReadValue("interface.getSpeed()")
        print(Speed)
        return Speed


t1 = threading.Thread(target=Setpoint)

t1.start()

ft.app(target=main)
