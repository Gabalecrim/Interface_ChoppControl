import flet as ft

def Login(page: ft.Page):
    
    return ft.View(
        "/",
        
        controls=[
            ft.Column([
                ft.Container(
                    ft.Image(
                        src=f"Interface\Assets\Big_Logo.png",
                        width=580,
                        height=175,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    padding=ft.padding.only(
                        top=10,
                        bottom=40,
                    ),
                ),
                ft.Container(
                    bgcolor ='#333740',
                    width= 480,
                    height= 540,
                    border_radius=10,

                    content= ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=40,
                                bottom=30,
                            ),
                            content=ft.Column([
                                ft.Text(
                                    value='Login',
                                    size=50,
                                    font_family='Poppins',
                                    weight='bold',  
                                )
                            ])
                        ),
                        ft.Column([
                            ft.TextField(
                                label="Username",
                                bgcolor='#242833',
                                width=300,
                                height=80,
                                border_radius=10,
                                border_width=2,
                                border_color='#242833',
                                prefix_icon=ft.icons.PERSON,
                            ),
                            ft.TextField(
                                label="Password",
                                password=True,
                                can_reveal_password=True,
                                bgcolor='#242833',
                                width=300,
                                height=80,
                                border_radius=10,
                                border_width=2,
                                border_color='#242833',
                                prefix_icon=ft.icons.LOCK,
                            ),
                        ]),
                        ft.Container(
                            ft.Checkbox(
                                label="Remember me",
                                value=False
                            ),
                            padding=ft.padding.only(
                                top=20,
                                bottom=12
                            )
                        ),
                        
                        ft.Container(
                            ft.CupertinoFilledButton(
                            content=ft.Text("Login"),
                            opacity_on_click=0.3,
                            on_click= lambda _: page.go("/")
                            ),
                            padding=ft.padding.only(
                            top=20,
                            bottom=12,
                            ),
                        ),
            
            ],horizontal_alignment='center')

        )
    ],horizontal_alignment='center')

        ]
    )
