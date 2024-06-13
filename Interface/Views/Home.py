import flet as ft
from flet import *
from flet_route import *


def Home(page: ft.Page, params: Params, basket: Basket):
    # ----------------------------------------------------------------
    # Navigation Bar
    class NavBar(UserControl):
        def UserData(self, initials: str):
            return Container(
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            on_click=lambda _: self.page.go("/next_view/:my_id"),
                            width=115,
                            height=115,
                            bgcolor="#333A40",
                            alignment=alignment.center,
                            border_radius=80,
                            content=Text(
                                value=initials,
                                size=35,
                                weight="Medium",
                                font_family="Poppins",
                            ),
                        )
                    ],
                )
            )

        def PageIcons(
            self,
            icon_name: str,
        ):
            return Container(
                width=90,
                height=150,
                border_radius=10,
                content=Row(
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        IconButton(
                            on_click=lambda _: self.page.go("/login"),
                            icon=icon_name,
                            icon_size=70,
                            icon_color=("#FFAF36"),
                            style=ButtonStyle(
                                color={MaterialState.HOVERED: colors.GREEN},
                            ),
                        )
                    ],
                ),
            )

        def build(self):
            return Container(
                width=200,
                height=982,
                padding=padding.only(top=10),
                alignment=alignment.center,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.UserData("GA"),
                        Divider(height=100, color="transparent"),
                        self.PageIcons(icons.SEARCH),
                        self.PageIcons(icons.DASHBOARD),
                        Divider(height=50, color="transparent"),
                        self.PageIcons(icons.SETTINGS),
                    ],
                ),
            )

    page.bgcolor = "#192026"
    menu = ft.Container(
        width=200,
        height=982,
        bgcolor=("#192026"),
        border_radius=10,
        alignment=ft.alignment.center,
        padding=20,
        content=NavBar(),
    )

    # Navigation Bar
    # ----------------------------------------------------------------
    # Header
    class Header(ft.UserControl):

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
                                        content=ft.PopupMenuButton(
                                            icon=ft.icons.NOTIFICATIONS_OUTLINED,
                                            icon_color=("#FFAF36"),
                                            icon_size=30,
                                        ),
                                    ),
                                    ft.Container(
                                        width=190,
                                        height=90,
                                        border_radius=80,
                                        bgcolor=("#192226"),
                                        padding=ft.padding.symmetric(horizontal=25),
                                        content=ft.Row(
                                            spacing=40,
                                            controls=[
                                                ft.PopupMenuButton(
                                                    icon=ft.icons.BUILD,
                                                    icon_color=("#FFAF36"),
                                                    icon_size=30,
                                                    items=[
                                                        ft.PopupMenuItem(text="Item 1"),
                                                        ft.PopupMenuItem(
                                                            icon=ft.icons.POWER_INPUT,
                                                            text="Check power",
                                                        ),
                                                        ft.PopupMenuItem(
                                                            content=ft.Row(
                                                                [
                                                                    ft.Icon(
                                                                        ft.icons.HOURGLASS_TOP_OUTLINED
                                                                    ),
                                                                    ft.Text(
                                                                        "Item with a custom content"
                                                                    ),
                                                                ]
                                                            ),
                                                            on_click=lambda _: print(
                                                                "Button with a custom content clicked!"
                                                            ),
                                                        ),
                                                        ft.PopupMenuItem(),  # divider
                                                        ft.PopupMenuItem(
                                                            text="Checked item",
                                                            checked=False,  # on_click=check_item_clicked
                                                        ),
                                                    ],
                                                ),
                                                ft.PopupMenuButton(
                                                    icon_color=("#FFAF36"),
                                                    icon_size=35,
                                                    icon=ft.icons.POWER_SETTINGS_NEW,
                                                    items=[
                                                        ft.PopupMenuItem(text="Item 1"),
                                                        ft.PopupMenuItem(
                                                            icon=ft.icons.POWER_INPUT,
                                                            text="Check power",
                                                        ),
                                                        ft.PopupMenuItem(
                                                            content=ft.Row(
                                                                [
                                                                    ft.Icon(
                                                                        ft.icons.HOURGLASS_TOP_OUTLINED
                                                                    ),
                                                                    ft.Text(
                                                                        "Item with a custom content"
                                                                    ),
                                                                ]
                                                            ),
                                                            on_click=lambda _: print(
                                                                "Button with a custom content clicked!"
                                                            ),
                                                        ),
                                                        ft.PopupMenuItem(),  # divider
                                                        ft.PopupMenuItem(
                                                            text="Checked item",
                                                            checked=False,  # on_click=check_item_clicked
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ]
                            )
                        ),
                    ],
                ),
            )

    # Header
    # ----------------------------------------------------------------
    # Status
    class Status(ft.UserControl):

        def build(self):
            Barril = 0

            def Start(e):

                def CloseDialog(e):
                    SemBarril.open = False
                    page.update()

                def OpenDialog(e):
                    page.dialog = SemBarril
                    SemBarril.open = True
                    page.update()

                if Barril == 0:
                    SemBarril = ft.AlertDialog(
                        content=ft.Text("Posicione um barril para iniciar o processo!"),
                        actions=[
                            ft.TextButton(
                                text="OK",
                                on_click=CloseDialog,
                            ),
                        ],
                    )
                    OpenDialog(e)
                else:
                    pass

            return ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Container(
                            height=100,
                            width=200,
                            border_radius=20,
                            bgcolor=("#192226"),
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=40, alignment=ft.alignment.center),
                    ft.Container(
                        ft.Image(
                            src=f"Interface\Assets\Barril.png",
                            width=200,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=40, alignment=ft.alignment.center),
                    ft.Container(
                        ft.CupertinoButton(
                            content=ft.Text(
                                "Start",
                                color=("#ffffff"),
                                font_family=("Poppins"),
                                weight=("Bold"),
                            ),
                            bgcolor=("#51BFF5"),
                            on_click=Start,
                        ),
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.alignment.center,
            )

    # Status
    # ----------------------------------------------------------------
    # Main page
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
                    padding=ft.padding.only(top=10, left=50),
                    content=Header(),
                ),
                # Status
                ft.Container(
                    width=1200,
                    height=800,
                    padding=ft.padding.only(top=10, left=100),
                    content=ft.Row(
                        spacing=100,
                        controls=[
                            # Space
                            ft.Container(
                                width=200,
                            ),
                            # Status
                            ft.Container(
                                width=450,
                                height=700,
                                padding=ft.padding.only(top=20),
                                content=Status(),
                            ),
                            # Dados
                            ft.Container(
                                width=500,
                                height=400,
                                padding=ft.padding.only(top=-50),
                                # content=Modules.Dados(),
                            ),
                        ],
                    ),
                ),
            ]
        ),
    )
    # Main pages
    # ----------------------------------------------------------------
    return ft.View(
        "/",
        controls=[
            ft.Container(
                width=1512,
                height=982,
                bgcolor="#192026",
                margin=ft.margin.all(30),
                content=ft.Row(controls=[menu, Process]),
            )
        ],
    )
