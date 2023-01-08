import os
import requests, json, os
from requests.auth import HTTPBasicAuth

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)
access_token = response.json()["access_token"]


artist = input("Artist: ").lower()
artist = artist.replace(" ", "%20")

url = "https://api.spotify.com/v1/search"
headers = {"Authorization": f"Bearer {access_token}"}
search = f"?q=artist%3A{artist}&type=track&limit=5"

full_url = f"{url}{search}"

response = requests.get(full_url, headers=headers)
data = response.json()

#print(json.dumps(data, indent=2))

for track in data["tracks"]["items"]:
    print(track["name"])
    print(track["preview_url"])