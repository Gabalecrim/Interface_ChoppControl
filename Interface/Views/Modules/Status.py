import flet as ft

class Status(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Container(
                        height=100,
                        width=200,
                        border_radius=20,
                        bgcolor=("#192226"),
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    height=40,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    ft.Image(
                        src=f"Interface\Assets\Galão.png",
                        width=200,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    height=40,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    ft.CupertinoButton(
                    content=ft.Text("Start", color=("#ffffff"), font_family=("Poppins"), weight=("Bold")),
                    bgcolor=("#51BFF5")
                    ),
                    alignment=ft.alignment.center
                ),
            ],alignment=ft.alignment.center            
        )
