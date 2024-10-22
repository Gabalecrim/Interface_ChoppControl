from flet import *


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
                                                "Kg",
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
