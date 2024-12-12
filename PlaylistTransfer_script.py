import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '98506f9a48be48c68e06d0eed3a31d0f'
CLIENT_SECRET = '4cb42f077e8d4bf5827bcf0a94402bdd'

# Configura l'autenticazione con le API di Spotify
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


# Funzione per ottenere dettagli della playlist
def get_playlist_tracks(playlist_url):
    # Estrai l'ID della playlist dall'URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Ottieni i dati della playlist
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    # Itera sulle tracce e stampa titolo e artista
    songs = []
    for item in tracks:
        track = item['track']
        song_name = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        songs.append(f"{song_name} by {artists}")

    return songs


# Inserisci il link della playlist Spotify
playlist_url = input("Enter the playlist url: ")
tracks = get_playlist_tracks(playlist_url)

# Stampa le tracce
for track in tracks:
    print(track)