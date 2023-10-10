import reflex as rx
import requests

from .base import State

class AuthState(State):
    username: str
    password: str
    confirm_password: str
    email: str
    scope: str = "me rates"
    logged: bool
    is_registered: bool = False

    def login(self):
        login = {
            "username": self.username,
            "password": self.password,
            "scope": self.scope
        }
        login_response = requests.post("http://16.170.146.0:10000/users/login",data=login)
        if login_response.status_code != 200:
            self.logged = False
            return rx.window_alert("Invalid username or password.")
        else:
            self.token = login_response.json()["access_token"]
            self.logged = True
            self.is_registered = False
            return rx.redirect("/home")
    
    def signup(self):
        if self.password != self.confirm_password:
            return rx.window_alert("Passwords do not match.")
        else:
            signup={
                "username": self.username,
                "hashed_password": self.password,
                "email": self.email
            }
            response = requests.post("http://16.170.146.0:10000/users/register",json=signup)
            if response.status_code != 201:
                return rx.window_alert(response.text)
            else:
                self.is_registered = True
                return rx.redirect("/login")



