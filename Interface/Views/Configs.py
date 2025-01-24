
import flet as ft
from flet import *
from flet_route import *
import threading
from Allan_utils import storage as st

class configStorage:

    @staticmethod
    def onChange(obj):
        if isinstance(obj,ControlEvent):
            valor = float(obj.control.value)
            label = obj.control.label
            label = str(label)
            label = label.replace(" " , "_")
            comando = ("st"+"."+label+"="+str(valor))
            exec(comando,{"st":st})

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
            Color: str,
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
                            icon_color=Color,
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
                        self.PageIcons(icons.DASHBOARD, ("#ffffff")),
                        Divider(height=50, color="transparent"),
                        self.PageIcons(icons.SETTINGS, ("#FFAF36")),
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
                                            icon=ft.icons.NOTIFICATIONS_OUTLINED,
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
                                content=ft.Container(
                                    content=ft.Column(
                                        controls=(
                                            [
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="SetPoint de fluxo",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                            
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="SetPoint de fluxo baixo",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                            
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="Velocidade servo ms",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="Velocidade do servo fim de envase ms",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="Set scale",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="Densidade",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="SetPoint_de_volume",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            label="Integral PIGid",
                                                            bgcolor="#192026",
                                                            border_radius=10,
                                                            border_width=2,
                                                            border_color="#192026",
                                                            prefix_icon=ft.icons.PERSON,
                                                            on_change=configStorage.onChange
                                                        ),
                                                        ft.CupertinoButton(
                                                            content=ft.Text(
                                                                "Set",
                                                                font_family="Pippins",
                                                                weight="Bold",
                                                                color=("#ffffff"),
                                                            ),
                                                            bgcolor="#FFAF36",
                                                            opacity_on_click=0.3,
                                                            # on_click=
                                                        ),
                                                    ],
                                                ),
                                            ]
                                        )
                                    ),
                                ),
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
