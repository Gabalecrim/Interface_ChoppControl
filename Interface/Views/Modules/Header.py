import flet as ft


class Header(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Container(
            ft.Row(
                spacing=580,
                controls=[
                    ft.Image(
                        src=f"Interface\Assets\Big_Logo.png",
                        width=350,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=90,
                                    height=90,
                                    border_radius=80,
                                    bgcolor=("#192226"),
                                ),
                                ft.Container(
                                    width=190,
                                    height=90,
                                    border_radius=80,
                                    bgcolor=("#192226"),
                                ),
                            ]
                        )
                    ),
                ],
            ),
        )
