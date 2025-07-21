import flet as ft
login_text = ft.Text('Login', weight=ft.FontWeight.BOLD, size=20),

def login_view(page: ft.Page):
    return ft.View(
        route="/login",
        controls=[
            ft.Text("Welcome back", size=50, weight="bold", font_family="Great Vibes", color=ft.Colors.BLUE),
            ft.Text("Log in to your account", size=15, color=ft.Colors.GREY),
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
                height=50,),
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
                height=50,),
            ft.Row([
                ft.CupertinoCheckbox(label="Remeber Me", value=True, height=40, width=40, active_color='#2474D9'),
                ft.TextButton(
                    content=ft.Text("forgot password ?", color=ft.Colors.BLUE),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
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
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Row([
                    ft.CupertinoButton(content=ft.Text("Login",size=22,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE), on_click=lambda e: page.go("/dashboard"), bgcolor='#2474D9', expand=True, padding=4, border_radius=8),
            ]),
            ft.Row([
                ft.Text("Don't have an account?"),
                ft.TextButton(content=ft.Text("Sign up", color=ft.Colors.BLUE), on_click=lambda e: page.go("/signup")),
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
