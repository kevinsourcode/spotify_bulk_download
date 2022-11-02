import spotipy
import csv,os,re

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv("spotif-names.env")

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
OUTPUT_FILE_NAME = "songmeta.csv"

PLAYLIST_LINK = "https://open.spotify.com/playlist/6e1dfJ7aJYPOXnIUEzHDpk"

#authenticate
client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)

session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_uri = "6e1dfJ7aJYPOXnIUEzHDpk"

songs = session.playlist_tracks(playlist_uri)["items"] #100 is max playlist length

with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["track","artist"])

    for track in songs:
        name = track["track"]["name"]
        artists = ", ".join([artist["name"] for artist in track["track"]["artists"]])

        writer.writerow([name, artists])




## get uri from https link
#if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", PLAYLIST_LINK):
 #   playlist_uri = match.groups()[0]
#else:
 #   raise ValueError("Expected format: https://open.spotify.com/playlist/...")