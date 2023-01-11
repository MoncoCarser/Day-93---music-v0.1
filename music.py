import os
import requests, json
from requests.auth import HTTPBasicAuth

def asking_for_songs_per_year(year):

#setting authenticators using Replit's secrets and guided authentication steps:
    client_id = os.environ['client_id']
    client_secret = os.environ['client_secret']
    
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type":"client_credentials"}
    auth = HTTPBasicAuth(client_id, client_secret)
    
    response = requests.post(url, data=data, auth=auth)
    access_token = response.json()["access_token"]
    
#if want to search based on artist:
    #artist = input("Artist: ").lower()
    #artist = artist.replace(" ", "%20")

#for this project we use year to get 10 top songs of that year
  #  year = input("Year: ")

    offset = 0
    
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    #search = f"?q=artist%3A{artist}&type=track&limit=5"
    search = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"
    
    full_url = f"{url}{search}"
    
    response = requests.get(full_url, headers=headers)
    data = response.json()

    return data

    #with this we can show the whole response in clearest form
    #print(json.dumps(data, indent=2))

    #to print only the song name and preview url:
    """for track in data["tracks"]["items"]:
        print(track["name"])
        print(track["preview_url"]) """                   