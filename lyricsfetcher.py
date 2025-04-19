import requests

def fetch_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("lyrics", "Lyrics not found.")
    else:
        return "Lyrics not available."
