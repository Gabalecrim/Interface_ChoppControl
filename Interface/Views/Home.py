import flet as ft
from flet import *
from flet_route import *
import threading


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
                content=ResponsiveRow(
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        IconButton(
                            on_click=lambda _: self.page.go("/configs"),
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
                                                ft.IconButton(
                                                    icon=ft.icons.BUILD,
                                                    on_click=lambda _: self.page.go(
                                                        "/configs"
                                                    ),
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
    # Status
    class Status(ft.UserControl):

        def build(self):
            Barril = 0
            enchimento = 200

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
                        content=ft.Container(
                            alignment=ft.alignment.center,
                            width=480,
                            height=600,
                            padding=15,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Divider(height=50, color="transparent"),
                                    ft.Image(
                                        src=f"Interface\Assets\Error.png",
                                        # width=200,
                                        # fit=ft.ImageFit.CONTAIN,
                                    ),
                                    ft.Divider(height=30, color="transparent"),
                                    ft.Text(
                                        "Erro",
                                        text_align=ft.TextAlign.CENTER,
                                        font_family=("Poppins"),
                                        weight="Bold",
                                        size=50,
                                    ),
                                    ft.Text(
                                        "Posicione o Barril!",
                                        text_align=ft.TextAlign.CENTER,
                                        font_family=("Poppins"),
                                        size=30,
                                    ),
                                    ft.Divider(height=60, color="transparent"),
                                    ft.CupertinoButton(
                                        content=ft.Text(
                                            "Ok",
                                            color=("#ffffff"),
                                            font_family=("Poppins"),
                                            weight=("Bold"),
                                        ),
                                        bgcolor=("#51BFF5"),
                                        on_click=CloseDialog,
                                    ),
                                ],
                            ),
                        ),
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
                    ft.Divider(height=40, color="transparent"),
                    ft.Container(
                        # alignment=ft.alignment.center,
                        content=ft.Stack(
                            [
                                ft.Container(
                                    width=264,
                                    height=368,
                                    alignment=ft.alignment.bottom_center,
                                    content=ft.Container(
                                        width=264,
                                        height=enchimento,
                                        bgcolor=("#FFAF36"),
                                    ),
                                ),
                                ft.Stack(
                                    [
                                        ft.Image(
                                            src=f"Interface\Assets\Barril_Status.png",
                                            width=265,
                                            height=368.61,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Container(
                                            width=264,
                                            height=364,
                                            padding=ft.padding.all(5),
                                            alignment=ft.alignment.center,
                                            content=ft.Text(
                                                "5L", size=50, font_family="Poppins"
                                            ),
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Divider(height=40, color="transparent"),
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
    # Dados
    class Dados(UserControl):

        def build(self):

            Velocidade = "50"
            Densidade = "1,08"
            Peso = "5,4"

            return Container(
                Column(
                    [
                        # Velocidade
                        Container(
                            bgcolor="#192226",
                            width=238,
                            height=160,
                            border_radius=10,
                            border=border.all(width=2, color=("#51BFF5")),
                            content=Column(
                                [
                                    Container(
                                        padding=padding.only(top=15, left=20),
                                        content=Row(
                                            vertical_alignment=CrossAxisAlignment.CENTER,
                                            spacing=5,
                                            controls=(
                                                Image(
                                                    src=f"Interface\Assets\Velocidade.png",
                                                    width=50,
                                                    height=50,
                                                    fit=ImageFit.CONTAIN,
                                                ),
                                                Text(
                                                    "Velocidade",
                                                    font_family="Poppins",
                                                    color=("#51BFF5"),
                                                    size=22,
                                                ),
                                            ),
                                        ),
                                    ),
                                    Container(
                                        padding=padding.only(left=50),
                                        content=Row(
                                            vertical_alignment=CrossAxisAlignment.END,
                                            spacing=40,
                                            controls=(
                                                Text(
                                                    f"{Velocidade}",
                                                    font_family="Poppins",
                                                    color=("#FFFFFF"),
                                                    size=40,
                                                ),
                                                Text(
                                                    "L/min",
                                                    font_family="Poppins",
                                                    color=("#8c9092"),
                                                    size=20,
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                                horizontal_alignment="center",
                            ),
                        ),
                        # Densidade
                        Container(
                            bgcolor="#192226",
                            width=238,
                            height=160,
                            border_radius=10,
                            content=Column(
                                [
                                    Container(
                                        padding=padding.only(top=15, left=28),
                                        content=Row(
                                            vertical_alignment=CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=(
                                                Image(
                                                    src=f"Interface\Assets\Densidade.png",
                                                    width=40,
                                                    height=42,
                                                    fit=ImageFit.CONTAIN,
                                                ),
                                                Text(
                                                    "Densidade",
                                                    font_family="Poppins",
                                                    color=("#51BFF5"),
                                                    size=22,
                                                ),
                                            ),
                                        ),
                                    ),
                                    Container(
                                        padding=padding.only(left=50),
                                        content=Row(
                                            vertical_alignment=CrossAxisAlignment.END,
                                            spacing=20,
                                            controls=(
                                                Text(
                                                    f"{Densidade}",
                                                    font_family="Poppins",
                                                    color=("#FFFFFF"),
                                                    size=40,
                                                ),
                                                Text(
                                                    "g/cm³",
                                                    font_family="Poppins",
                                                    color=("#8c9092"),
                                                    size=20,
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                                horizontal_alignment="center",
                            ),
                        ),
                        # Peso
                        Container(
                            bgcolor="#192226",
                            width=238,
                            height=160,
                            border_radius=10,
                            content=Column(
                                [
                                    Container(
                                        padding=padding.only(top=25, left=35),
                                        content=Row(
                                            vertical_alignment=CrossAxisAlignment.CENTER,
                                            spacing=15,
                                            controls=(
                                                Image(
                                                    src=f"Interface\Assets\Peso.png",
                                                    width=30,
                                                    height=30,
                                                    fit=ImageFit.CONTAIN,
                                                ),
                                                Text(
                                                    "Peso",
                                                    font_family="Poppins",
                                                    color=("#51BFF5"),
                                                    size=22,
                                                ),
                                            ),
                                        ),
                                    ),
                                    Container(
                                        padding=padding.only(left=50),
                                        content=Row(
                                            vertical_alignment=CrossAxisAlignment.END,
                                            spacing=40,
                                            controls=(
                                                Text(
                                                    f"{Peso}",
                                                    font_family="Poppins",
                                                    color=("#FFFFFF"),
                                                    size=40,
                                                ),
                                                Text(
                                                    "kg",
                                                    font_family="Poppins",
                                                    color=("#8c9092"),
                                                    size=20,
                                                ),
                                            ),
                                        ),
                                    ),
                                ],
                                horizontal_alignment="center",
                            ),
                        ),
                    ],
                    horizontal_alignment="center",
                )
            )

    # Dados
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
                                col=2
                            ),
                            # Status
                            ft.Container(
                                width=450,
                                height=700,
                                col=6,
                                padding=ft.padding.only(top=20, right=10),
                                content=Status(),
                            ),
                            # Dados
                            ft.Container(
                                width=500,
                                height=400,
                                col=4,
                                padding=ft.padding.only(top=-50, right=10),
                                content=Dados(),
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
