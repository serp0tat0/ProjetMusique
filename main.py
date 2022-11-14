import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = "Radiohead" #input("insert artist name\n")

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]

toptracks = spotify.artist_top_tracks(artist['uri'])
trackindex = 1
for track in toptracks['tracks'][:10]:

    print(trackindex, track["name"])
    trackindex += 1
