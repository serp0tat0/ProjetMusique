import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pylast
from passwords_ts import name, password, secret, key
import lfmxtractplus as lxp
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import calmap as cm
from IPython.display import display, HTML
import os
import configparser


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


    network = pylast.LastFMNetwork(
        api_key=key,
        api_secret=secret,
        username=name,
        password_hash=password,



    )
    pylast.User.get_top_track("Chad_musica", "12month", 50, )

"""
using lfmxtractplus
"""
lf = lxp.lfmxtractplus("config.yaml")
scrobbles_dict = lf.generate_dataset(lfusername = 'Chad_musica', pages = 0)
scrobbles_df = scrobbles_dict['complete']


# note that this is for python3. Some changes need to be made for python2

# create parser object and read config file
config = configparser.RawConfigParser()
config.read('myconfig.cfg')

# loop through. Here for instructional purposes we print, but you can
# assign etc instead.
for section in config.sections():
    print(section)
    for option in config.options(section):
        text = '{} {}'.format(option, config.get(section,option))
        print(text)
