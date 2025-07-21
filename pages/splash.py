import flet as ft

def splash_view(page: ft.Page):
    # Fallback static splash icon (no Lottie dependency)
    splash_icon = ft.Container(
        content=ft.Icon(
            name=ft.Icons.ROCKET_LAUNCH,
            size=100,
            color=ft.Colors.WHITE
        ),
        alignment=ft.alignment.center
    )

    # Timer-based redirection to login page (without asyncio)
    def on_timer_tick(e):
        page.go("/login")

    # Start a timer that triggers once after 5 seconds
    page.timer(
        interval=5000,  # milliseconds
        repeat=False,
        on_tick=on_timer_tick
    )

    # Splash screen controls
    controls = [
        splash_icon,
        ft.Container(height=20),
        ft.Text(
            "Welcome to Flet App", 
            size=24, 
            weight=ft.FontWeight.BOLD, 
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER
        ),
    ]

    # Return splash view with background gradient
    return ft.View(
        route="/",
        controls=controls,
        bgcolor=ft.Colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                col
