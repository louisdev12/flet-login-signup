import flet as ft
from pages.splash import splash_view
from pages.login import login_view
from pages.signup import signup_view
from pages.dashboard import dashboard_view

def main(page: ft.Page):
    page.title = "Flet App"
    page.window_width = 400
    page.window_height = 700
    page.padding = 0    
    page.spacing = 0
    page.scroll = ft.ScrollMode.HIDDEN
    page.bgcolor = ft.Colors.TRANSPARENT
    page.safe_area = True
    page.window.to_front()
    page.theme_mode = ft.ThemeMode.DARK
    page.notch_shape = ft.NotchShape.AUTO

    # ✅ Add Great Vibes font
    page.fonts = {
        "Great Vibes": "https://raw.githubusercontent.com/google/fonts/master/ofl/greatvibes/GreatVibes-Regular.ttf"
    }

    # ✅ Unified theme setup
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.CUPERTINO,
        ),
        scrollbar_theme=ft.ScrollbarTheme(thickness=0.0)
    )

    # ✅ Navigation handling
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(splash_view(page))
        elif page.route == "/login":
            page.views.append(login_view(page))
        elif page.route == "/signup":
            page.views.append(signup_view(page))
        elif page.route == "/dashboard":
            page.views.append(dashboard_view(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(target=main)