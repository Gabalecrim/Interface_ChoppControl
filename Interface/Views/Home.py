import flet as ft
from flet_route import *
import Modules


def Home(page: ft.Page):
    page.bgcolor = "#1e1e1e"
    menu = ft.Container(
        width=200,
        height=982,
        border_radius=10,
        alignment=ft.alignment.center,
        padding=20,
        content=Modules.NavBar(),
    )

    Process = ft.Container(
        width=1305,
        height=982,
        bgcolor="#333A40",
        border_radius=ft.border_radius.only(top_left=30, bottom_left=30),
        alignment=ft.alignment.center,
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                # Header
                ft.Container(
                    padding=ft.padding.only(top=10, left=50), content=Modules.Header()
                ),
                # main page
                ft.Container(
                    width=1200,
                    height=800,
                    padding=ft.padding.only(top=10, left=100),
                    content=ft.Row(
                        spacing=50,
                        controls=[
                            ft.Container(
                                width=500,
                                height=700,
                                bgcolor=("#192226"),
                            ),
                            ft.Container(
                                width=500, height=400, content=Modules.Dados()
                            ),
                        ],
                    ),
                ),
            ]
        ),
    )

    main = ft.Container(
        width=1512,
        height=982,
        bgcolor="#192026",
        margin=ft.margin.all(30),
        content=ft.Row(controls=[menu, Process]),
    )

    page.add(main)
    page.update()


ft.app(target=Home)
