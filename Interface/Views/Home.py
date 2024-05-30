import flet as ft
from flet_route import *
from flet import *

class NavBar(UserControl):
    def __init__(self):
        super().__init__()

    def UserData(self, initials: str):
        return Container(
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        on_click= lambda _: self.page.go("/login"),
                        width=85,
                        height=85,
                        bgcolor='#333A40',
                        alignment=alignment.center,
                        border_radius=42,
                        content=Text(
                            value=initials,
                            size=30,
                            weight="Medium",
                            font_family="Poppins"
                        )
                    )
                ]
            )
        )

    def PageIcons(self, icon_name:str,):
        return Container(
            width=90,
            height=150,
            border_radius=10,
            content=Row(
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    IconButton(
                        on_click= lambda _: self.page.go("/login"),
                        icon=icon_name,
                        icon_size=70,
                        icon_color=('#ffffff'),
                        style=ButtonStyle(
                            color={
                                MaterialState.HOVERED: colors.GREEN
                            },
                        )
                    )
                ]
            )
        )

    def build(self):
        return Container(
            width=200,
            height=780,
            padding=padding.only(top=20),
            alignment=alignment.center,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.UserData("GA"),
                    Divider(height=50, color='transparent'),
                    self.PageIcons(icons.SEARCH),
                    self.PageIcons(icons.DASHBOARD),
                    Divider(height=50, color='transparent'),
                    self.PageIcons(icons.SETTINGS)
                ]
            )
            
        )
def Home(page: Page):
    page.add(
        Container(
            width=200,
            height=800,
            bgcolor='#192226',
            border_radius=10,
            alignment=alignment.center,
            padding=20,
            content=NavBar()
        )
    )
    page.update()

app(target=Home)

'''
def Home(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/asd",

        controls=[
            ft.Container(
                width=200,
                height=780,
                bgcolor='#192026',
                border_radius=10,
                alignment=ft.alignment.center,
                padding=20,
                Controls=[
                    NavBar()
                ],

            )
            
        ]
    )
'''

