import flet as ft

def signup_view(page: ft.Page):
    return ft.View(
        route="/signup",
        controls=[
            ft.Text("Create Account", size=50, weight="bold", font_family="Great Vibes", color=ft.Colors.BLUE),
            ft.Text("Sign up to get started", size=15, color=ft.Colors.GREY),

            ft.TextField(
                label="Full Name",
                filled=True,
                cursor_color=ft.Colors.BLUE,
                fill_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                border_color='#374151',
                border_radius=12,
                prefix_icon=ft.Icons.PERSON,
                focused_border_color='#2474D9',
                label_style=ft.TextStyle(color=ft.Colors.GREY, size=16),
                text_style=ft.TextStyle(color=ft.Colors.WHITE, size=15),
                height=50,
            ),

            ft.TextField(
                label="Email",
                filled=True,
                cursor_color=ft.Colors.BLUE,
                fill_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                border_color='#374151',
                border_radius=12,
                prefix_icon=ft.Icons.EMAIL,
                focused_border_color='#2474D9',
                label_style=ft.TextStyle(color=ft.Colors.GREY, size=16),
                text_style=ft.TextStyle(color=ft.Colors.WHITE, size=15),
                height=50,
            ),

            ft.TextField(
                label="Password",
                password=True,
                can_reveal_password=True,
                filled=True,
                cursor_color=ft.Colors.BLUE,
                fill_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                border_color='#374151',
                border_radius=12,
                prefix_icon=ft.Icons.LOCK,
                focused_border_color='#2474D9',
                label_style=ft.TextStyle(color=ft.Colors.GREY, size=16),
                text_style=ft.TextStyle(color=ft.Colors.WHITE, size=15),
                height=50,
            ),

            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Text("─── or continue with ───", size=19, color=ft.Colors.GREY),
            ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
            ft.Row([
                ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE),
                    border_radius=50,
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src="assets/brands/Google.png",
                        width=35,
                        height=35,
                        fit=ft.ImageFit.CONTAIN
                    )
                ),
                ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE),
                    border_radius=50,
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src="assets/brands/microsoft.png",
                        width=35,
                        height=35,
                        fit=ft.ImageFit.CONTAIN
                    )
                ),
                ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE),
                    border_radius=50,
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src="assets/brands/apple.png",
                        width=35,
                        height=35,
                        fit=ft.ImageFit.CONTAIN
                    )
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.CupertinoButton(
                    content=ft.Text("Sign Up", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    on_click=lambda e: page.go("/dashboard"),
                    bgcolor="#2474D9",
                    expand=True,
                    padding=4,
                    border_radius=8
                ),
            ]),

            ft.Row([
                ft.Text("Already have an account?", color=ft.Colors.GREY),
                ft.TextButton(
                    content=ft.Text("Login", color=ft.Colors.BLUE),
                    on_click=lambda e: page.go("/login")
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ],
        bgcolor=ft.Colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#10162c", "#0c2749", "#0f0f23", "#1a1a2e"],
                tile_mode=ft.GradientTileMode.MIRROR
            )
        ),
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
