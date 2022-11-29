import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pylast




def spotifytest():
    scope="user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    def get_auth(message):
        username = str(message.from_user.id)
        scope = "user-top-read"
        auth = SpotifyOAuth(
            redirect_uri="http://localhost:8000",
            username=username,
            scope=scope
        )
        return auth

    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = input("insert artist name\n") #gives the top 10 for any given artist

    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]

    toptracks = sp.artist_top_tracks(artist['uri'])
    trackindex = 1
    for track in toptracks['tracks'][:10]:

        print(trackindex, track["name"])
        trackindex += 1

    scope = "user-library-read"

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
    API_KEY = "6f2418af4811729422f66602cad71f14"
    USER_AGENT = "Chad_musica"
    import requests

    headers = {
        'user-agent': USER_AGENT
    }

    payload = {
        'api_key': API_KEY,
        'method': 'chart.gettopartists',
        'format': 'json'
    }

    r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    r.status_code


    # Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
    # to get more help about anything and see examples of how it works

lastfmTest()