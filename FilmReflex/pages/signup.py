import reflex as rx
from FilmReflex.state.auth import AuthState
from ..components import container

def signup():
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
            rx.input(
                type_="password",
                placeholder="Confirm password",
                on_blur=AuthState.set_confirm_password,
                mb=4,
            ),
            rx.input(placeholder="Email", on_blur=AuthState.set_email, mb=4),
            rx.button(
                "Sign up",
                on_click=AuthState.signup,
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
        rx.text(
            "Already have an account?  ",
            rx.link("Sign in here.", href="/login", color="blue.500"),
            color="gray.600",
            style={"text-align": "center"},
        ),
    )