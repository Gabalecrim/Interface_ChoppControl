import flet as ft
from flet_route import Routing, path
from Views.Home import Home
from Views.Login import Login


def main(page: ft.Page):

    app_routes = [
        path(
            url="/",  # Here you have to give that url which will call your view on mach
            clear=True,  # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=Home().view,  # Here you have to pass a function or method which will take page,params and basket and return ft.View (If you are using function based view then you just have to give the name of the function.)
        ),
        path(url="/next_view/:my_id", clear=False, view=Login),
    ]

    Routing(
        page=page,  # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes,  # Here a list has to be passed in which we have defined app routing like app_routes
    )
    page.go(page.route)


ft.app(target=main)
