import requests 

apiKey = "b923f853"

params = {
    "t": "The Godfather",
    "apikey": apiKey
}

url = "http://www.omdbapi.com/"

resp= requests.get(url, params=params)

print(resp.json())


class Actor(model.Model):
    

class Movie(model.Model):
    title
    year
    actors = []
    genre = 

class Genre(mod):
    name

