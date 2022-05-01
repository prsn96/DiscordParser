import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth())

artist= "Jack Kays"
track = "MY HEAD :("
track_id = sp.search(q="artist:" + artist + " track:" + track, type="track")
print(track_id['id'])