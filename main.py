import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

"""


spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = input("insert artist name\n") #gives the top 10 for any given artist

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]

toptracks = spotify.artist_top_tracks(artist['uri'])
trackindex = 1
for track in toptracks['tracks'][:10]:

    print(trackindex, track["name"])
    trackindex += 1
"""
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

sp.current_user()

results = sp.current_user_saved_tracks(limit=50)
for idx, item in enumerate(results["items"]):
    idx += 1
    track = item["track"]
    print(idx, track["artists"][0]["name"], " - ", track["name"])
results = sp.current_user_saved_tracks(limit=50, offset=50)
for idx, item in enumerate(results["items"]):
    idx += 51
    track = item["track"]
    print(idx, track["artists"][0]["name"], " - ", track["name"])
