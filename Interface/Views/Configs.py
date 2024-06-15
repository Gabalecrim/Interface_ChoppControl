import flet as ft
from flet import *
from flet_route import *
import threading


def Configs(page: ft.Page, params: Params, basket: Basket):
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
                content=ResponsiveRow(
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        IconButton(
                            on_click=lambda _: self.page.go("/"),
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
                        self.PageIcons(icons.DASHBOARD),
                        Divider(height=50, color="transparent"),
                        self.PageIcons(icons.SETTINGS),
                    ],
                ),
            )

    menu = ft.Container(
        width=200,
        height=982,
        # bgcolor=("#192026"),
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
                alignment=ft.alignment.center_right,
                content=ft.ResponsiveRow(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=120,
                            height=120,
                            col=4,
                            # alignment=ft.alignment.center,
                            content=ft.Image(
                                src=f"Interface\Assets\Big_Logo.png",
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ),
                        ft.Container(
                            width=120,
                            height=120,
                            col=4,
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            col=4,
                            content=ft.Row(
                                controls=[
                                    ft.CircleAvatar(
                                        # border_radius=80,
                                        radius=45,
                                        bgcolor=("#192226"),
                                        content=ft.IconButton(
                                            style=ft.ButtonStyle(
                                                color=("#FFAF36"),
                                                # bgcolor=("Transparent"),
                                            ),
                                            icon=ft.Icon(
                                                name=ft.icons.NOTIFICATIONS_OUTLINED,
                                                color=("#FFAF36"),
                                            ),
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
                                                            content=ft.ResponsiveRow(
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
                            ),
                        ),
                    ],
                ),
            )

    # Header
    # ----------------------------------------------------------------
    class Inputs(ft.UserControl):
        def build(self):
            return ft.Container(
                alignment=ft.alignment.top_center,
                content=ft.Column(
                    controls=[
                        ft.SegmentedButton(
                            selected={1},
                            segments=[
                                ft.Segment(
                                    value="1",
                                    label=ft.Text("Fluxo"),
                                    icon=ft.Icon(ft.icons.LOOKS_ONE),
                                ),
                                ft.Segment(
                                    value="2",
                                    label=ft.Text("Processo"),
                                    icon=ft.Icon(ft.icons.LOOKS_ONE),
                                ),
                            ],
                        )
                    ]
                ),
            )

    # ----------------------------------------------------------------
    # Main page
    Process = ft.Container(
        bgcolor="#333A40",
        border_radius=ft.border_radius.only(
            top_left=30, bottom_left=30, top_right=5, bottom_right=5
        ),
        alignment=ft.alignment.center,
        # padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                # Header
                ft.Container(
                    padding=ft.padding.only(top=10, left=50, right=10),
                    content=Header(),
                ),
                # Status
                ft.Container(
                    # padding=ft.padding.only(top=10, left=100, right=10),
                    content=ft.ResponsiveRow(
                        expand=True,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        # spacing=100,
                        controls=[
                            # Space
                            ft.Container(
                                # width=200,
                                col=3
                            ),
                            # Status
                            ft.Container(
                                width=450,
                                height=700,
                                col=6,
                                padding=ft.padding.only(top=20, right=10),
                                content=Inputs(),
                            ),
                            # Dados
                            ft.Container(
                                width=500,
                                height=400,
                                col=3,
                                padding=ft.padding.only(top=-50, right=10),
                                # content=Dados(),
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
        bgcolor="#192026",
        controls=[
            ft.Container(
                expand=True,
                # bgcolor="#ffffff",
                # padding=ft.padding.only(top=10, left=10, bottom=10, right=10),
                # margin=ft.margin.all(30),
                content=ft.ResponsiveRow(
                    expand=True,
                    controls=[
                        ft.Container(content=menu, col=2),
                        ft.Container(content=Process, col=10),
                    ],
                ),
            )
        ],
    )
