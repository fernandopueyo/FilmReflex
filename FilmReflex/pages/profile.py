import reflex as rx
from FilmReflex.state.profile import ProfileState
from FilmReflex.state.base import State
from ..components import container

def profile():
    return container(
        rx.link(
            rx.image(
            src="/logo.png",
            width="auto",
            height="30px",
            position="absolute",
            top="0px",
            left="0px"
            ),
            href="http://localhost:3000/home/"
        ),
        rx.cond(
            State.user_login,
            rx.link(
                rx.avatar(size="xs"),
                href="/profile",
                position="absolute",
                top="0px",
                right="0px",
            ),
            rx.link(
                rx.button("Login / Sign up", size="xs"),
                href="/login",
                position="absolute",
                top="0px",
                right="0px",  
            )
        ),
        rx.vstack(
            rx.text("Profile"),
            rx.divider(border_color="black"),
            rx.grid(
                rx.grid_item(
                    rx.vstack(
                        rx.text("Username", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                        rx.text("Full name", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                        rx.text("Email", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                    ),
                    row_span=2,
                    col_span=1
                ),
                rx.grid_item(
                    rx.vstack(
                        rx.text(ProfileState.username, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                        rx.text(ProfileState.full_name, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                        rx.text(ProfileState.email, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                    ),
                    row_span=4,
                    col_span=3
                ),
                rx.grid_item(
                        rx.button(
                            "My ratings.", on_click=ProfileState.right, size="sm"
                        ),
                        rx.drawer(
                            rx.drawer_overlay(
                                rx.drawer_content(
                                    rx.drawer_header("My ratings"),
                                    rx.drawer_body(
                                        rx.vstack(
                                            rx.foreach(ProfileState.rates_list, lambda row,index:
                                                       rx.vstack(
                                                           rx.link(row.primaryTitle, href=ProfileState.films_link[index]),
                                                           rx.text(row.rate),
                                                       ))
                                        )
                                    ),
                                    rx.drawer_footer(
                                        rx.button(
                                            "Close", on_click=ProfileState.right
                                        )
                                    ),
                                    bg="rgba(0, 0, 0, 0.3)",
                                )
                            ),
                            is_open=ProfileState.show_right,
                        ),  
                ),
                template_rows="repeat(4, 1fr)",
                template_columns="repeat(6, 1fr)",
                width="100%",
                gap=4                
            ),
        ),
    )