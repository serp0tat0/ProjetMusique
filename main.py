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
    results = sp.search(q=r'artist:' + artist_name, type=r'artist')
    items = results[r'artists'][r'items']
    artists = None
    if len(items) > 0:
        artist = items[0]
        artist_id = artist[r'id']
        similar_artists = sp.artist_related_artists(artist_id)
        artists = similar_artists[r'artists']
    else:
        print(r"Couldn't find artist with name " + artist_name)

        # Define the artist to get simsilar artists for

        # Get the list of similar artists
    similar_artists = artists

        # Extract the artist names and popularity scores
    artist_names = [artist[r'name'] for artist in similar_artists]
    popularity_scores = [artist[r'popularity'] for artist in similar_artists]

    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(popularity_scores, range(len(artist_names)), alpha=0.5)

    # Add labels and title
    ax.set_xlabel(r'Popularity')
    ax.set_ylabel(r'Artist')
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


def GigaJuicer(playlist_id, threshold):
    sartist_counts = {}
    playlist = sp.playlist_tracks(playlist_id=playlist_id, fields=r"items(track(name, artists(name)))")

    # Count the occurrence of artists in the playlist
    artist_counts = {}
    for item in playlist["items"]:
        track = item["track"]
        for artist in track["artists"]:
            artist_name = artist["name"]
            if artist_name in artist_counts:
                artist_counts[artist_name] += 1
            else:
                artist_counts[artist_name] = 1

    # Get similar artists for each artist and count their occurrence
    processed_artists = set()  # Keep track of already processed artists
    for item in playlist["items"]:
        track = item["track"]
        for artist in track["artists"]:
            artist_name = artist["name"]
            if artist_name in processed_artists:
                continue  # Skip processing if the artist has already been processed

            processed_artists.add(artist_name)  # Add the artist to the set of processed artists

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

            if artists is not None:
                for artist in artists:
                    similar_artist_name = artist['name']
                    if similar_artist_name in sartist_counts:
                        sartist_counts[similar_artist_name] += 1
                    else:
                        sartist_counts[similar_artist_name] = 1

    # Filter similar artists based on the threshold percentage
    total_artists = sum(artist_counts.values())
    filtered_similar_artists = {
        artist: count for artist, count in sartist_counts.items()
        if count >= threshold
    }
    num_similar_artists = len(filtered_similar_artists)
    if num_similar_artists > 0:
        print("Number of similar artists shown:", num_similar_artists)
    else:
        print("No similar artists meet the threshold criteria.")

    sorted_similar_artists = sorted(filtered_similar_artists.items(), key=lambda x: x[1], reverse=True)
    sartists = [a[0] for a in sorted_similar_artists]
    counts = [a[1] for a in sorted_similar_artists]
    plt.barh(np.arange(len(sartists)), counts)
    plt.yticks(np.arange(len(sartists)), sartists)
    plt.xlabel("Number of times seen")
    plt.title("Playlist artists")
    plt.show()

GigaJuicer("2NAWvom8XiRN8th60fqZmv", 3)