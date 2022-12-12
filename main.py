import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pylast as pyla
from passwords_ts import name, password, secret, key



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


def lastfmTest():


    # You have to have your own unique two values for API_KEY and API_SECRET
    # Obtain yours from https://www.last.fm/api/account/create for Last.fm


    network = pyla.LastFMNetwork(
        api_key=key,
        api_secret=secret,
        username=name,
        password_hash=password,
    )


    pyla.Alb
lastfmTest()