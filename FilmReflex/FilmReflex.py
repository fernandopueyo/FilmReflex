"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import requests

from .pages import home, film, login, signup, profile
from .state.base import State
from .state.film import FilmState
from .state.profile import ProfileState

app = rx.App(state=State)
app.add_page(home, on_load=State.check_login())
app.add_page(film, route="/film/[pid]", on_load=[FilmState.get_film(), State.check_login()])
app.add_page(login)
app.add_page(signup)
app.add_page(profile, on_load=[ProfileState.get_user(), State.check_login()])

app.compile()

