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
                        on_click=lambda _: self.page.go("/login"),
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
