import numpy as np
import spotipy
import spotipy.util as util
import pandas as pd
import time
from passwords_ts import sp_cid, sp_secret, playlist_id
import networkx as nx
import matplotlib.pyplot as plt
username = 'Nathcamaroti'
scope = 'user-library-read'
client_id = sp_cid
client_secret = sp_secret
redirect_uri = 'http://localhost:8000'
global sp
"""
Connection 
"""


def login():
    token = util.prompt_for_user_token(
        username = username, scope = scope,
        client_id = client_id, client_secret = client_secret,
        redirect_uri = redirect_uri)
    global sp
    sp = spotipy.Spotify(auth=token)

login()
#SIMILAR ARTISTS TESTING
global artist_name


def get_similar_artists(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    artists = None
    if len(items) > 0:
        artist = items[0]
        artist_id = artist['id']
        similar_artists = sp.artist_related_artists(artist_id)
        artists = similar_artists['artists']
    else:
        print("Couldn't find artist with name " + artist_name)

        # Define the artist to get simsilar artists for

        # Get the list of similar artists
    similar_artists = artists

        # Extract the artist names and popularity scores
    artist_names = [artist['name'] for artist in similar_artists]
    popularity_scores = [artist['popularity'] for artist in similar_artists]

    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(popularity_scores, range(len(artist_names)), alpha=0.5)

    # Add labels and title
    ax.set_xlabel('Popularity')
    ax.set_ylabel('Artist')
    ax.set_title(f'Similar Artists to {artist_name}')

    # Add artist names as y-axis labels
    ax.set_yticks(range(len(artist_names)))
    ax.set_yticklabels(artist_names)

    # Show the plot
    plt.show()
#get_similar_artists("Sjammienators")

#playlist reading, stuff like that, and whatnot, going to add the option for the user to pick a playlist straight up, because Ion wanna mess w that rn
#DOING THE PLAYLIST SELECTION RN... JK
def ILOVEPLAYLISTREADING(playlist_id):
    playlist = sp.playlist_tracks( playlist_id=playlist_id, fields="items(track(name, artists(name)))")
    for item in playlist["items"]:
        track = item["track"]
        for artist in track["artists"]:
            print(artist["name"])


    artist_counts = {}


    for item in playlist["items"]:
        track = item["track"]
        for artist in track["artists"]:
            if artist["name"] in artist_counts:
                artist_counts[artist["name"]] += 1
            else:
                artist_counts[artist["name"]] = 1


    #sort the artists by number of tracks
    sorted_artists = sorted(artist_counts.items(), key = lambda x: x[1], reverse=True)
    artists =  [a[0] for a in sorted_artists]
    counts = [a[1] for a in sorted_artists]
    plt.barh(np.arange(len(artists)), counts)
    plt.yticks(np.arange(len(artists)), artists)
    plt.xlabel("Number of tracks")
    plt.title("Playlist artists")
    plt.show()
#ILOVEPLAYLISTREADING()

def GigaJuicer(playlist_id):

    playlist = sp.playlist_tracks( playlist_id=playlist_id, fields="items(track(name, artists(name)))")
    for item in playlist["items"]:
        track = item["track"]
        for artist in track["artists"]:
            print(artist["name"])
            artist_name = artist["name"]
            results = sp.search(q='artist:' + artist_name, type='artist')
            items = results['artists']['items']
            artists = None
            if len(items) > 0:
                artist = items[0]
                artist_id = artist['id']
                similar_artists = sp.artist_related_artists(artist_id)
                artists = similar_artists['artists']
            else:
                print("Couldn't find artist with name " + artist_name)

                # Define the artist to get simsilar artists for

                # Get the list of similar artists

            for artist in artists:
                print(artist['name'])

GigaJuicer("3CLDVpuAwUudpk6vs3L3O7")
#TESTING THIS ARRAY BULLSHIT