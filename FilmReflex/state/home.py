import reflex as rx
import requests

from .base import State, Film

class HomeState(State):
    text: str = "Look for a movie..."
    title: str
    films_list: list[Film]
    looking_database: bool = False
    first_search = True
    format_link = "/film/{}"
    films_link: list[str]

    def clear_search(self):
        self.first_search = True

    def set_text(self, text: str):
        self.text = requests.get(f"http://16.170.146.0:10000/films/name/{text}").text

    async def search_films_title(self):
        self.looking_database = True
        self.first_search = False
        yield
        films_list_db = requests.get(f"http://16.170.146.0:10000/films/name/{self.title}").json()
        self.looking_database = False
        self.films_list = [Film(**film) for film in self.films_schema(films_list_db)]
        self.films_link = [self.get_film_link(film.id) for film in self.films_list]

    def film_schema(self, film) -> dict:
        return {
            "id": film["id"],
            "title": film["primaryTitle"] if film["primaryTitle"] is not None else "N/A",
            "year": str(film["startYear"]) if film["startYear"] is not None else "N/A",
            "genres": film["genres"] if film["genres"] is not None else "N/A",
            "runtime": film["runtimeMinutes"] if film["runtimeMinutes"] is not None else "N/A",
            "averageRating": str(film["averageRating"]) if film["averageRating"] is not None else "N/A",
            "numVotes": str(film["numVotes"]) if film["numVotes"] is not None else "N/A"
        }
    
    def films_schema(self, films) -> list[dict]:
        return [self.film_schema(film) for film in films]
    
    def get_film_link(self, id) -> str:
        return self.format_link.format(id)
    
