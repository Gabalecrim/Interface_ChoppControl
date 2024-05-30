import flet as ft
from flet_route import *
from flet import *
import Modules

def Home(page: Page):
    page.bgcolor="#1e1e1e"
    menu=ft.Container(
        width=200,
        height=982,
        border_radius=10,
        alignment=alignment.center,
        padding=20,
        content=Modules.SideBar()
        )
    
    Process=ft.Container(
        width=1305,
        height=982,
        bgcolor='#333A40',
        border_radius=border_radius.only(top_left=30, bottom_left=30),
        alignment=alignment.center,
    )
    
    main = ft.Container(
        width=1512,
        height=982,
        bgcolor= '#192026',
        margin=ft.margin.all(30),
        content=ft.Row(
            controls=[
                menu,
                Process
            ]
        )
    )

    page.add(main)
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

