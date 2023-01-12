import os
import requests, json
from requests.auth import HTTPBasicAuth
from replit import db



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
    
    #offset causes web page to show different songs as same year is requested again. 
    #BUT code like this is skipping the start of the list(?), so this is commented out for now and web page only shows the first 10 from data
    offset = 0
    """try:
        offset = db[year]
        if offset > 50:
            db[year] = 0
        db[year] += 10
    except:
        db[year] = 10"""
    
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


    

#below func takes the data from above and put the 3 requested details on a html template that shows on the webpage /top_10_of_the_year
    
def print_song(year):
    page = ""
    f = open("./templates/template.html", "r")
    page = f.read()
    f.close
    data = asking_for_songs_per_year(year)
    music_list = ""
    for track in data["tracks"]["items"]:
        song = page
        song = song.replace("{song}", track["name"])
        song = song.replace("{artist}", track["artists"][0]["name"])
        song = song.replace("{url}", track["preview_url"])
        music_list += song
    return music_list