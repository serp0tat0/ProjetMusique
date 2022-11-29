import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pylast




def spotifytest():
    spotify = spotipy.Spotify(SpotifyOAuth.)

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

def lastfmTest():
    # You have to have your own unique two values for API_KEY and API_SECRET
    # Obtain yours from https://www.last.fm/api/account/create for Last.fm
    API_KEY = "b25b959554ed76058ac220b7b2e0a026"  # this is a sample key
    API_SECRET = "425b55975eed76058ac220b7b4e8a054"

    # In order to perform a write operation you need to authenticate yourself
    username = "your_user_name"
    password_hash = pylast.md5("your_password")

    network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=username,
        password_hash=password_hash,
    )

    # Now you can use that object everywhere
    track = network.get_track("Iron Maiden", "The Nomad")
    track.love()
    track.add_tags(("awesome", "favorite"))

    # Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
    # to get more help about anything and see examples of how it works

spotifytest()