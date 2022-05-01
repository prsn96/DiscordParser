import requests
import pandas
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

def add_track(track):
    scope = "playlist-modify-private"
    playlist="1zVo3iNaf9Hk2edSOwK7YB"
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_add_items(playlist_id=playlist,items=track)

def check_tracks(id):
    playlist="1zVo3iNaf9Hk2edSOwK7YB"
    