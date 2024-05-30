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
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(
                            src=f"Interface\Assets\Big_Logo.png",
                            width=350,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Container(
                            width=90,
                            height=90,
                            border_radius=80,
                            bgcolor=("#192226"),
                        ),
                        ft.Container(
                            width=170,
                            height=90,
                            border_radius=80,
                            bgcolor=("#192226"),
                        ),
                    ],
                ),
                ft.Row(controls=[]),
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
