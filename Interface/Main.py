import flet as ft
from flet_route import Routing, path
from Views.Home import Home
from Views.Login import Login
from Views.Configs import Configs
import time
import threading


def main(page: ft.Page):
    """
    Main function to start the application.

    Args:
        page (ft.Page): The main page of the application.
    """
    # Set the background color of the window
    page.window_bgcolor = "#192026"
    # Set the title of the window
    page.title = "Chopp Control"
    # Set the minimum height of the window
    page.window_min_height = 700
    # Set the minimum width of the window
    page.window_min_width = 1000

    # Define the routes for the application
    app_routes = [
        path(
            url="/",
            clear=True,  # Clear all other views before adding the Home view
            view=Home,  # View to show when the root URL is accessed
        ),
        path(
            url="/next_view/:my_id",
            clear=False,  # Add the Login view to the existing views
            view=Login,  # View to show when the URL /next_view/:my_id is accessed
        ),
        path(
            url="/configs",
            clear=False,  # Add the Configs view to the existing views
            view=Configs,  # View to show when the URL /configs is accessed
        ),
    ]

    # Initialize routing with the main page and the defined routes
    Routing(
        page=page,
        app_routes=app_routes,
    )
    # Start the application by navigating to the initial route
    page.go(page.route)


ft.app(target=main)
