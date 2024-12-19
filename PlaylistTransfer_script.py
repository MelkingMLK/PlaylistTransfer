import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Credenziali Spotify
CLIENT_ID = '98506f9a48be48c68e06d0eed3a31d0f'
CLIENT_SECRET = '4cb42f077e8d4bf5827bcf0a94402bdd'
EMAIL = "sashalessandro17@gmail.com"
PASSWORD = "minecraft17"
# Configurazione autenticazione con Spotify
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Funzione per ottenere tutte le tracce della playlist
def get_playlist_tracks(playlist_url):
    # Estrai l'ID della playlist dall'URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Lista che conterrà tutte le tracce
    all_tracks = []
    offset = 0
    limit = 100  # Spotify restituisce massimo 100 tracce per chiamata

    # Loop per ottenere tutte le tracce
    while True:
        # Ottieni un blocco di tracce con offset e limit
        results = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        tracks = results['items']

        # Aggiungi le tracce ottenute alla lista principale
        all_tracks.extend(tracks)

        # Verifica se ci sono altre tracce
        if len(tracks) < limit:
            # Se il numero delle tracce è minore del limite, hai finito
            break
        offset += limit  # Aggiorna l'offset per la prossima "pagina"

    # Itera su tutte le tracce e stampa titolo e artista
    c = 1
    for item in all_tracks:
        track = item['track']
        song_name = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        print(f"{c}: {song_name} by {artists}")
        c += 1

# Inserisci il link della playlist Spotify
playlist_url = input("Enter the playlist URL: ")
get_playlist_tracks(playlist_url)
#v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^
driver = webdriver.Safari()
try:
    driver.get("https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fmusic.amazon.it%2F%3Freferer%3Dhttps%253A%252F%252Fmusic.amazon.it%252F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_webamp_it&openid.mode=checkid_setup&language=it_IT&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=login&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    time.sleep(1)  # Attendi il caricamento della pagina

    email_input = driver.find_element(By.ID, "ap_email")
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        body_element = driver.find_element(By.TAG_NAME, "Annulla")  # Focalizza sul corpo della pagina
        body_element.send_keys(Keys.ESCAPE)  # Simula la pressione di ESC
        time.sleep(1)
        print("Pop-up chiuso con ESC.")
    except Exception as e:
        print(f"Errore nel chiudere il pop-up con ESC: {str(e)}")
    # 4. Inserisci la password
    password_input = driver.find_element(By.ID, "ap_password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Attendi il completamento del login


    print("Login effettuato con successo!")
finally:
    # Chiude il browser
    driver.quit()
















































































