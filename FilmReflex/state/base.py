import reflex as rx
import requests
from sqlmodel import Field
from typing import Optional
from pydantic import BaseModel

class Film(rx.Model):
    id: str
    title: str
    year: str
    genres: str
    runtime: str 
    averageRating: str
    numVotes: str

class User(rx.Model):
    id: str
    username: str
    password: str
    email: str

class Rate(rx.Model):
    film_id: str
    primaryTitle: str
    user_id: str
    username: str
    rate: str

class State(rx.State):
    token: str
    user_login: bool = False
    
    def check_login(self):
        try:
            headers= {'Authorization': f'Bearer {self.token}'}
            response = requests.get("http://16.170.146.0:10000/users/status",headers=headers)
            if response.status_code == 200:
                self.user_login = True
            else:
                self.user_login = False
        except:
            self.user_login = False