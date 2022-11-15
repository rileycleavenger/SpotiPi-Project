#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="38d6c9a24eec445288edb097eafc59dc"
CLIENT_SECRET="ba41a77481be4f4b865cc77ad0cdf65b"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080",
                                                scope="user-read-playback-state,user-modify-playback-state"))


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:5omHiTR0fMTT1Etz9T5Vsc')