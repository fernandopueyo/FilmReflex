import reflex as rx
from FilmReflex.state.auth import AuthState
from ..components import container

def login():
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
        rx.box(
            rx.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.button(
                "Log in",
                on_click=AuthState.login,
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
                mb=4,
            ),
            margin="auto",
            bg="white",
            border="1px solid #eaeaea",
            p=4,
            max_width="400px",
            border_radius="lg",
            display="flex",  
            flex_direction="column",  
            align_items="center",  
            justify_content="center",  
        ),
        rx.cond(
            AuthState.is_registered,
            rx.alert(
                rx.alert_icon(),
                rx.alert_title("Successful registration."),
                status="success",
                max_width="400px",
                margin="auto",
            ),
            rx.text(
                "Don't have an account yet? ",
                rx.link("Sign up here.", href="/signup", color="blue.500"),
                color="gray.600",
                style={"text-align": "center"},
            ),
        )

    )