import reflex as rx
import requests

from .base import State
from .auth import AuthState

class FilmState(State):
    id: str
    title: str
    year: str
    genres: str
    runtime: str
    averageRating: str
    numVotes: str
    userRate: str
    rate_options = list(range(0,11))

    @rx.var
    def film_id(self):
        return self.get_query_params().get("pid", "no pid")
    
    def get_film(self):
        film = requests.get(f"http://16.170.146.0:10000/films/id/{self.film_id}").json()
        return self.film_schema(film)
    
    def film_schema(self, film):
        self.id =  film["id"]
        self.title =  film["primaryTitle"] if film["primaryTitle"] is not None else "N/A"
        self.year = str(film["startYear"]) if film["startYear"] is not None else "N/A"
        self.genres = film["genres"] if film["genres"] is not None else "N/A"
        self.runtime = film["runtimeMinutes"] if film["runtimeMinutes"] is not None else "N/A"
        self.averageRating = str(film["averageRating"]) if film["averageRating"] is not None else "N/A"
        self.numVotes = str(film["numVotes"]) if film["numVotes"] is not None else "N/A"

    def rate_film(self, rate):
        try:
            rate = float(rate)
            url = f'http://16.170.146.0:10000/films/id/{self.id}/?rate={rate}'
            token = self.token
            headers= {'Authorization': f'Bearer {token}'}
            response = requests.post(url,headers=headers)
            if response.status_code != 200:
                if response.json()["detail"] == "Rate already exists":
                    response = requests.put(url,headers=headers)
                else:
                    return rx.window_alert(response.text)
        except:
            pass
