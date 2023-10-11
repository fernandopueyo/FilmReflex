import reflex as rx
from FilmReflex.state.film import FilmState
from FilmReflex.state.base import State
from ..components import container

def film():
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
            rx.text(FilmState.title),
            rx.divider(border_color="black"),
            rx.grid(
                rx.grid_item(
                    rx.vstack(
                        rx.text("Title", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                        rx.text("Year", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                        rx.text("Genres", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                        rx.text("Run time", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}),
                        rx.text("Num Votes", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"})
                    ),
                    row_span=2,
                    col_span=1
                ),
                rx.grid_item(
                    rx.vstack(
                        rx.text(FilmState.title, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                        rx.text(FilmState.year, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                        rx.text(FilmState.genres, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                        rx.text(FilmState.runtime, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}),
                        rx.text(FilmState.numVotes, style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"})
                    ),
                    row_span=4,
                    col_span=3
                ),
                rx.grid_item(
                    rx.vstack(
                        rx.text("Avg Rating", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "font-weight": "bold"}),
                        rx.hstack(
                            rx.icon(tag="star"),
                            rx.text(FilmState.averageRating)
                        ),
                        rx.text("Your rate", style={"font-family": "Helvetica, sans-serif", "font-size": "10px", "font-weight": "bold"}),
                        rx.cond(
                            State.user_login,
                            rx.select(
                                FilmState.rate_options,
                                placeholder="Rate film",
                                on_change=FilmState.rate_film,
                                color_schemes="twitter",
                                size="xs"
                            ),
                            rx.text("Login to rate.", style={"font-family": "Helvetica, sans-serif", "font-size": "8px", "font-weight": "bold"})                            
                        ),
                    ),
                    col_start=-1,
                    col_span=1,
                    row_span=1,
                ),
                template_rows="repeat(4, 1fr)",
                template_columns="repeat(6, 1fr)",
                width="100%",
                gap=4
            )
        )
    )
    
