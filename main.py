import spotipy
import spotipy.util as util
import pandas as pd
import time
from passwords_ts import sp_cid, sp_secret
import networkx as nx
import matplotlib.pyplot as plt
username = 'Nathcamaroti'
scope = 'user-library-read'
client_id = sp_cid
client_secret = sp_secret
redirect_uri = 'https://example.com/callback'

token = util.prompt_for_user_token(
    username = username, scope = scope,
    client_id = client_id, client_secret = client_secret,
    redirect_uri = redirect_uri)

sp = spotipy.Spotify(auth=token)

# Define function to get similar artists for a given artist
def get_similar_artists(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        artist_id = artist['id']
        similar_artists = sp.artist_related_artists(artist_id)
        return similar_artists['artists']
    else:
        print("Couldn't find artist with name " + artist_name)

# Define the artist to get similar artists for
artist_name = input("insert artist name\n")

# Get the list of similar artists
similar_artists = get_similar_artists(artist_name)

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
playlist_id = "2ioMrZinG1MptQSyUiXTD0"
sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist_id)
tracks = sp_playlist["items"]
print(tracks)
