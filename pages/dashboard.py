import flet as ft

def dashboard_view(page: ft.Page):

    def create_story(avatar_color, name, is_own=False):
        border_color = ft.Colors.PINK_400 if not is_own else ft.Colors.GREY_600
        return ft.Column([
            ft.Container(
                content=ft.Container(
                    content=ft.Text(name[0].upper(), size=16, weight="bold", color=ft.Colors.WHITE),
                    width=50, height=50,
                    bgcolor=avatar_color,
                    border_radius=25,
                    alignment=ft.alignment.center
                ),
                padding=3,
                border=ft.border.all(2, border_color),
                border_radius=28,
                width=56, height=56
            ),
            ft.Text(name if len(name) <= 8 else name[:8], size=12, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4)

    def create_post(username, avatar_color, time_ago, content, likes_count, comments, shares):
        like_icon = ft.Ref[ft.IconButton]()
        save_icon = ft.Ref[ft.IconButton]()
        likes_text = ft.Ref[ft.Text]()
        state = {"liked": False, "saved": False}

        def toggle_like(e):
            state["liked"] = not state["liked"]
            like_icon.current.icon = ft.Icons.FAVORITE if state["liked"] else ft.Icons.FAVORITE_BORDER
            like_icon.current.icon_color = ft.Colors.RED if state["liked"] else ft.Colors.WHITE
            count = int(likes_text.current.value)
            likes_text.current.value = str(count + 1 if state["liked"] else count - 1)
            page.update()

        def toggle_save(e):
            state["saved"] = not state["saved"]
            save_icon.current.icon = ft.Icons.BOOKMARK if state["saved"] else ft.Icons.BOOKMARK_BORDER
            save_icon.current.icon_color = ft.Colors.BLUE if state["saved"] else ft.Colors.WHITE
            page.update()

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        content=ft.Text(username[0].upper(), size=14, weight="bold", color=ft.Colors.WHITE),
                        width=40, height=40,
                        bgcolor=avatar_color,
                        border_radius=20,
                        alignment=ft.alignment.center
                    ),
                    ft.Column([
                        ft.Text(username, size=14, weight="bold", color=ft.Colors.WHITE),
                        ft.Text(time_ago, size=12, color=ft.Colors.GREY_400)
                    ], spacing=2, expand=True),
                    ft.IconButton(ft.Icons.MORE_HORIZ, icon_color=ft.Colors.GREY_400, icon_size=20)
                ], spacing=12),
                ft.Text(content, size=14, color=ft.Colors.WHITE),
                ft.Container(
                    height=200,
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    border_radius=12,
                    content=ft.Icon(ft.Icons.IMAGE_OUTLINED, size=40, color=ft.Colors.GREY_600),
                    alignment=ft.alignment.center
                ),
                ft.Row([
                    ft.Row([
                        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_color=ft.Colors.WHITE, icon_size=22, ref=like_icon, on_click=toggle_like),
                        ft.Text(str(likes_count), color=ft.Colors.GREY_400, size=13, ref=likes_text)
                    ], spacing=4),
                    ft.Row([
                        ft.IconButton(ft.Icons.CHAT_BUBBLE_OUTLINE, icon_color=ft.Colors.WHITE, icon_size=20),
                        ft.Text(str(comments), color=ft.Colors.GREY_400, size=13)
                    ], spacing=4),
                    ft.Row([
                        ft.IconButton(ft.Icons.SHARE_OUTLINED, icon_color=ft.Colors.WHITE, icon_size=20),
                        ft.Text(str(shares), color=ft.Colors.GREY_400, size=13)
                    ], spacing=4),
                    ft.IconButton(icon=ft.Icons.BOOKMARK_BORDER, icon_color=ft.Colors.WHITE, icon_size=20, ref=save_icon, on_click=toggle_save)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ], spacing=12),
            padding=16,
            margin=ft.margin.symmetric(horizontal=16, vertical=8),
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
            border_radius=16
        )

    return ft.View(
        route="/dashboard",
        appbar=ft.AppBar(
            bgcolor=ft.Colors.with_opacity(0.0, ft.Colors.BLACK),
            elevation=0,
            title=ft.Text("Social App", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE, font_family="Great Vibes"),
            center_title=False,
            actions=[
                ft.IconButton(ft.Icons.FAVORITE_BORDER, icon_color=ft.Colors.WHITE),
                ft.IconButton(ft.Icons.CHAT_BUBBLE_OUTLINE, icon_color=ft.Colors.WHITE),
                ft.PopupMenuButton(
                    content=ft.Container(
                        content=ft.Text("JD", size=14, weight="bold", color=ft.Colors.WHITE),
                        width=32, height=32,
                        bgcolor=ft.Colors.BLUE_600,
                        border_radius=16,
                        alignment=ft.alignment.center
                    ),
                    items=[
                        ft.PopupMenuItem(text="Profile", icon=ft.Icons.PERSON),
                        ft.PopupMenuItem(text="Settings", icon=ft.Icons.SETTINGS),
                        ft.PopupMenuItem(text="Logout", icon=ft.Icons.LOGOUT, on_click=lambda e: page.go("/login"))
                    ]
                )
            ]
        ),
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Row([
                            create_story(ft.Colors.GREY_600, "Your Story", True),
                            create_story(ft.Colors.PINK_400, "Alice"),
                            create_story(ft.Colors.GREEN_400, "Bob"),
                            create_story(ft.Colors.ORANGE_400, "Charlie"),
                            create_story(ft.Colors.PURPLE_400, "Diana")
                        ], scroll=ft.ScrollMode.AUTO, spacing=16),
                        padding=ft.padding.symmetric(horizontal=20, vertical=16)
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Container(
                                content=ft.Text("JD", size=14, weight="bold", color=ft.Colors.WHITE),
                                width=40, height=40,
                                bgcolor=ft.Colors.BLUE_600,
                                border_radius=20,
                                alignment=ft.alignment.center
                            ),
                            ft.TextField(
                                hint_text="What's on your mind?",
                                expand=True,
                                bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                                border_radius=20,
                                border_color=ft.Colors.TRANSPARENT,
                                focused_border_color=ft.Colors.BLUE,
                            ),
                            ft.IconButton(ft.Icons.PHOTO_CAMERA, icon_color=ft.Colors.BLUE_400, icon_size=24),
                        ], spacing=12),
                        padding=ft.padding.symmetric(horizontal=20, vertical=8),
                        margin=ft.margin.only(bottom=8)
                    ),
                    ft.Container(
                        content=ft.Column([
                            create_post("Alice Johnson", ft.Colors.PINK_400, "2h ago", 
                                      "Just finished an amazing workout! 💪", 
                                      24, 8, 3),
                            create_post("Bob Smith", ft.Colors.GREEN_400, "4h ago", 
                                      "Beautiful sunset today! 🌅", 
                                      156, 23, 12),
                            create_post("Charlie Brown", ft.Colors.ORANGE_400, "6h ago", 
                                      "Trying out a new recipe today! 🍝", 
                                      67, 15, 5),
                            create_post("Diana Prince", ft.Colors.PURPLE_400, "8h ago", 
                                      "Weekend adventures! 🏞️", 
                                      89, 19, 8)
                        ], spacing=0, scroll=ft.ScrollMode.AUTO),
                        expand=True
                    )
                ], scroll=ft.ScrollMode.AUTO),
                expand=True
            )
        ],
        bgcolor=ft.Colors.TRANSPARENT,
        decoration=ft.BoxDecoration(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0f0f23", "#1a1a2e", "#16213e", "#0f3460"],
                tile_mode=ft.GradientTileMode.MIRROR
            )
        ),
        padding=0
    )
