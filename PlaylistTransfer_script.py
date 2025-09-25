import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import random

# Credenziali Spotify
CLIENT_ID = '98506f9a48be48c68e06d0eed3a31d0f'
CLIENT_SECRET = '4cb42f077e8d4bf5827bcf0a94402bdd'
REDIRECT_URI = "http://localhost:8888/callback"
EMAIL = "sashalessandro17@gmail.com"
PASSWORD = "minecraft17"
# Configurazione autenticazione con Spotify
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
SCOPE = "playlist-modify-public playlist-modify-private playlist-read-private"

# Playlist di destinazione dove salvare le 20 canzoni random
DESTINATION_PLAYLIST_ID = "spotify:playlist:https://open.spotify.com/playlist/2dzMh4qsgWHHKBA2d3ffl0?si=6a700732aaa348e1"

# --- AUTENTICAZIONE ---
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# --- INPUT DA CONSOLE ---
source_playlist_url = input("Inserisci l'URL o l'ID della playlist sorgente: ").strip()

# Normalizza l’ID della playlist (tolgo "spotify:playlist:" o l'URL)
if "playlist" in source_playlist_url:
    playlist_id = source_playlist_url.split("playlist/")[1].split("?")[0]
else:
    playlist_id = source_playlist_url

# --- OTTIENI NUMERO DI TRACCE TOTALI ---
playlist_info = sp.playlist(playlist_id, fields="tracks.total")
total_tracks = playlist_info["tracks"]["total"]

print(f"La playlist contiene {total_tracks} canzoni.")

# --- GENERA 20 INDICI RANDOM ---
random_indices = random.sample(range(total_tracks), 20)

# --- RECUPERA I 20 BRANI ---
track_uris = []
for idx in random_indices:
    results = sp.playlist_items(playlist_id, offset=idx, limit=1, fields="items(track.uri)")
    if results["items"]:
        track_uris.append(results["items"][0]["track"]["uri"])

print("Brani scelti:")
for uri in track_uris:
    print(uri)

# --- SVUOTA LA PLAYLIST DI DESTINAZIONE ---
sp.playlist_replace_items(DESTINATION_PLAYLIST_ID, [])

# --- AGGIUNGI I NUOVI BRANI ---
sp.playlist_add_items(DESTINATION_PLAYLIST_ID, track_uris)




































































