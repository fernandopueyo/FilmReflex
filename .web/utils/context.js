import { createContext } from "react"
import { Event, hydrateClientStorage } from "/utils/state.js"

export const initialState = {"auth_state": {"confirm_password": "", "email": "", "is_registered": false, "logged": 0, "password": "", "scope": "me rates", "username": ""}, "film_state": {"averageRating": "", "film_id": "no pid", "genres": "", "id": "", "numVotes": "", "rate_options": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "runtime": "", "title": "", "userRate": "", "year": ""}, "home_state": {"films_link": [], "films_list": [], "first_search": true, "format_link": "/film/{}", "looking_database": false, "text": "Look for a movie...", "title": ""}, "is_hydrated": false, "pid": "", "profile_state": {"email": "", "films_link": [], "format_link": "http://localhost:3000/film/{}", "full_name": "", "rates_list": [], "show_right": false, "username": ""}, "token": "", "user_login": false}
export const StateContext = createContext(null);
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}}
export const initialEvents = [
    Event('state.hydrate', hydrateClientStorage(clientStorage)),
]