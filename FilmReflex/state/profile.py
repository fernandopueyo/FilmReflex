import reflex as rx
import requests
from .base import State, Rate

class ProfileState(State):
    username: str
    email: str
    full_name: str
    rates_list: list[Rate]
    show_right: bool = False
    format_link = "/film/{}"
    films_link: list[str]

    def get_user(self):
        headers= {'Authorization': f'Bearer {self.token}'}
        response = requests.get("http://16.170.146.0:10000/users/me",headers=headers)
        if response.status_code == 200:
            user = response.json()
            self.username = user["username"] if user["username"] is not None else "N/A"
            self.email = user["email"] if user["email"] is not None else "N/A"
            self.full_name = user["full_name"] if user["full_name"] is not None else "N/A"
            rate_response = requests.get("http://16.170.146.0:10000/users/me/rates",headers=headers)
            if rate_response.json():
                rates_list_db = rate_response.json()
                self.rates_list = [Rate(**rate) for rate in self.rates_schema(rates_list_db)]
                self.films_link = [self.get_film_link(film.film_id) for film in self.rates_list]
            else:
                self.rates_list = []
        else:
            rx.redirect("/login")

    def rate_schema(self, rate) -> dict:
        return {
            "film_id": rate["film_id"],
            "primaryTitle": rate["primaryTitle"] if rate["primaryTitle"] is not None else "N/A",
            "user_id": rate["user_id"] if rate["user_id"] is not None else "N/A",
            "username": rate["username"] if rate["username"] is not None else "N/A",
            "rate": str(rate["rate"]) if rate["rate"] is not None else "N/A",
        }
    
    def rates_schema(self, rates) -> list[dict]:
        return [self.rate_schema(rate) for rate in rates]
    
    def right(self):
        self.show_right = not (self.show_right)

    def get_film_link(self, id) -> str:
        return self.format_link.format(id)