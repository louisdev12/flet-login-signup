import flet as ft
import flet_lottie as fl
import asyncio

def splash_view(page: ft.Page):
    # Try to load Lottie animation with error handling
    lottie_widget = None
    try:
        lottie_widget = fl.Lottie(
            src_base64='/lottie.json',
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
            repeat=True,
            background_loading=True,
            animate=True,
        )
    except Exception as e:
        print(f"Error loading Lottie animation: {e}")
        # Fallback to an icon if there's any error
        lottie_widget = ft.Container(
            content=ft.Icon(
                ft.Icons.ROCKET_LAUNCH,
                size=100,
                color=ft.Colors.WHITE
            ),
        )

    # Auto-navigate to login after 5 seconds
    async def auto_navigate():
        await asyncio.sleep(5)
        page.go("/login")
    
    page.run_task(auto_navigate)

    # Create controls list
    controls = []
    if lottie_widget:
        controls.append(lottie_widget)
    
    controls.extend([
        ft.Container(height=20),  # Spacing
        ft.Text(
            "Welcome to Flet App", 
            size=24, 
            weight=ft.FontWeight.BOLD, 
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER
        ),
    ])

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
