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
                                    content=ft.PopupMenuButton(
                                                icon=ft.icons.NOTIFICATIONS_OUTLINED,
                                                icon_color=("#FFAF36"),
                                                icon_size=30,
                                    )
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
                                                    ft.PopupMenuItem(icon=ft.icons.POWER_INPUT, text="Check power"),
                                                    ft.PopupMenuItem(
                                                        content=ft.Row(
                                                            [
                                                                ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                                                                ft.Text("Item with a custom content"),
                                                            ]
                                                        ),
                                                        on_click=lambda _: print("Button with a custom content clicked!"),
                                                    ),
                                                    ft.PopupMenuItem(),  # divider
                                                    ft.PopupMenuItem(
                                                        text="Checked item", checked=False, #on_click=check_item_clicked
                                                    ),
                                                ]
                                            ),
                                            ft.PopupMenuButton(
                                                icon_color=("#FFAF36"),
                                                icon_size=35,
                                                icon=ft.icons.POWER_SETTINGS_NEW,
                                                items=[
                                                    ft.PopupMenuItem(text="Item 1"),
                                                    ft.PopupMenuItem(icon=ft.icons.POWER_INPUT, text="Check power"),
                                                    ft.PopupMenuItem(
                                                        content=ft.Row(
                                                            [
                                                                ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                                                                ft.Text("Item with a custom content"),
                                                            ]
                                                        ),
                                                        on_click=lambda _: print("Button with a custom content clicked!"),
                                                    ),
                                                    ft.PopupMenuItem(),  # divider
                                                    ft.PopupMenuItem(
                                                        text="Checked item", checked=False, #on_click=check_item_clicked
                                                    ),
                                                ]
                                            ),
                                        ]
                                    )
                                    
                                ),
                            ]
                        )
                    ),
                ],
            ),
        )
