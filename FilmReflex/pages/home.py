import reflex as rx
from FilmReflex.state.base import State, Film
from FilmReflex.state.home import HomeState
from ..components import container

def home():
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
            href="/"
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
            rx.hstack(
                rx.input(
                    placeholder="Look for a movie",
                    on_change=HomeState.set_title,
                    style={"max-width": "400px", "font-family": "Helvetica, sans-serif", "font-size": "12px"}
                ),
                rx.button(
                    "Search", 
                    on_click=HomeState.search_films_title(),
                    is_loading=HomeState.looking_database,
                    style={"max-width": "100px", "font-family": "Helvetica, sans-serif", "font-size": "8px"}
                )
            ),
            rx.cond(
                HomeState.first_search,
                rx.text(""),
                rx.table_container(
                    rx.table(
                        rx.thead(
                            rx.tr(
                                rx.th("Title"),
                                rx.th("Year"),
                                rx.th("Genres"),
                                rx.th("Runtime"),
                                rx.th("Avg Rating"),
                                rx.th("Num Votes")
                            ),
                            style={"font-family": "Helvetica, sans-serif", "font-size": "12px"}
                        ),
                        rx.tbody(
                        rx.foreach(HomeState.films_list, lambda row, index: rx.tr(
                            rx.td(rx.link(row.title, href=HomeState.films_link[index]), style={"max_width": "490px", "white-space": "normal", "padding": "1px"}),
                            rx.td(row.year, style={"max_width": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}),
                            rx.td(row.genres, style={"max_width": "150px", "white-space": "normal", "text-align": "center", "padding": "1px"}),
                            rx.td(row.runtime, style={"max_width": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}),
                            rx.td(row.averageRating, style={"max_width": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}),
                            rx.td(row.numVotes, style={"max_width": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"})
                            )),
                            style={"font-family": "Arial, sans-serif", "font-size": "8px"}
                        )
                    )
                )
            )  
        )
    )