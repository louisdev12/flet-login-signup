import flet as ft
import asyncio

def splash_view(page: ft.Page):
    # Async task to navigate after 5 seconds
    async def auto_navigate():
        await asyncio.sleep(5)
        page.go("/login")

    # Start the task
    page.run_task(auto_navigate)

    # Just fallback icon (since no Lottie used)
    icon_widget = ft.Container(
        content=ft.Icon(
            ft.Icons.ROCKET_LAUNCH,
            size=100,
            color=ft.Colors.WHITE
        ),
    )

    # Controls for the splash screen
    controls = [
        icon_widget,
        ft.Container(height=20),  # Spacer
        ft.Text(
            "Welcome to Flet App",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER
        ),
    ]

    return ft.View(
        route="/",
        controls=controls,
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
        padding=20,
    )
