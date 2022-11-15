#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="38d6c9a24eec445288edb097eafc59dc"
CLIENT_SECRET="ba41a77481be4f4b865cc77ad0cdf65b"

while True:
   try:
       reader = SimpleMFRC522()
       sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET,
                                                      redirect_uri="http://localhost:8080",
                                                      scope="user-read-playback-state,user-modify-playback-state"))

       # create an infinite while loop that will always be waiting for a new scan
       while True:
           print("Waiting for record scan...")
           id = reader.read()[0]
           print("Card Value is:", id)
           sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

           # DONT include the quotation marks around the card's ID value, just paste the number
           if (id == 4890142461):

               # playing a song
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:5omHiTR0fMTT1Etz9T5Vsc')
               sleep(2)

           elif (id == 557511976612):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:3n7PS7D0DNpD3o13bVLTQN')
               sleep(2)

           elif (id == 489214420547):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6X1x82kppWZmDzlXXK3y3q')
               sleep(2)


           elif (id == 966489449986):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5BGzOpea6At0Nd7tYtYZOP')
               sleep(2)

           elif (id == 764139447999):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0WzOtZBpXvWdNdH7hCJ4qo')
               sleep(2)

           elif (id == 73424938712):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6sDQacCej53Q43vZF9PJ8i')
               sleep(2)

           elif (id == 142459774703):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1xpGyKyV26uPstk1Elgp9Q')
               sleep(2)

           elif (id == 830712620633):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2RKEso6nin3nhRyAd36Omv')
               sleep(2)

           elif (id == 418882364949):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2BtE7qm1qzM80p9vLSiXkj')
               sleep(2)

           elif (id == 622976214653):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4JTOxuvM2jcSqAvEZtZsOO')
               sleep(2)

           elif (id == 554575373948):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:2oZjYwPmqzhU5f0HUeYyTF')
               sleep(2)

           elif (id == 760549320262):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5wtE5aLX5r7jOosmPhJhhk')
               sleep(2)

           elif (id == 829101286948):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1ntNLgaYCFCkeW4flGYlY2')
               sleep(2)

           elif (id == 8293164550):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1UcS2nqUhxrZjrBZ3tHk2N')
               sleep(2)

           elif (id == 899482363465):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2kqn09pydzvKvB3xWbAxY4')
               sleep(2)

           elif (id ==760264238675 ):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1bt6q2SruMsBtcerNVtpZB')
               sleep(2)

           elif (id == 829017335338):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:artist:2YOYua8FpudSEiB9s88IgQ')
               sleep(2)

           elif (id == 418009687749):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, uris='spotify:track:6Q1KlB6kpTwPKspzSzYhKV')
               sleep(2)

           elif (id == 144744752705):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4SZko61aMnmgvNhfhgTuD3')
               sleep(2)

           elif (id == 966725379584):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2nkto6YNI4rUYTLqEwWJ3o')
               sleep(2)

           elif (id == 761976235564):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0S0KGZnfBGSIssfF54WSJh')
               sleep(2)

           elif (id == 899736446579):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:392p3shh2jkxUxY2VHvlH8')
               sleep(2)

           elif (id == 279432111771):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1YZ3k65Mqw3G8FzYlW1mmp')
               sleep(2)

           elif (id == 8041440822):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:621OhgnZJ7Pz8iUazct1In')
               sleep(2)

           elif (id == 1036822947398):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1YgekJJTEueWDaMr7BYqPk')
               sleep(2)

           elif (id == 557481174684):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:78iX7tMceN0FsnmabAtlOC')
               sleep(2)


           elif (id == 214286247431):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:5zi7WsKlIiUXv09tbGLKsE')
               sleep(2)

           elif (id == 554259752543):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4UG3kz6qoHtNI1glQ2wdon')
               sleep(2)

           elif (id == 348134876813):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:0USMC6cVglCmWH670gWw6k')
               sleep(2)

           elif (id == 622979229263):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1btu0SV2DOI5HoFsvUd78F')
               sleep(2)

           elif (id == 1036000667154):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2XgBQwGRxr4P7cHLDYiqrO')
               sleep(2)

           elif (id == 555467580929):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6trNtQUgC8cgbWcqoMYkOR')
               sleep(2)

           elif (id == 967361799741):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7HVoV2lgVsmuiHsjbbUJB4')
               sleep(2)

           elif (id == 486748104433):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:42oBdomfxF0DbKKMEqrnQW')
               sleep(2)

           elif (id == 1039001167605):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, uris='spotify:track:48kwdkeHEJEuMzcKklPv5b')
               sleep(2)

           elif (id == 145916470834):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4Hai0uVzRbyTSaTPzxTY4e')
               sleep(2)

           elif (id == 210643101394):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2ODvWsOgouMbaA5xf0RkJe')
               sleep(2)

           elif (id == 145446577680):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4Carzsnpd6yvuHZ49I0oz8')
               sleep(2)

           elif (id == 420022429253):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4eLPsYPBmXABThSJ821sqY')
               sleep(2)

           elif (id == 213763139092 ):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4GNIhgEGXzWGAefgN5qjdU')
               sleep(2)

           elif (id == 832339224292):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:21ENdNQSHkmT9qfbzLF26C')
               sleep(2)

           elif (id == 691745891916):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:45ba6QAtNrdv6Ke4MFOKk9')
               sleep(2)

           elif (id ==488691443288):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6kZ42qRrzov54LcAk4onW9')
               sleep(2)

           elif (id == 760297662039):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4yP0hdKOZPNshxUOjY0cZj')
               sleep(2)

           elif (id == 899484329579):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2nLOHgzXzwFEpl62zAgCEC')
               sleep(2)

           elif (id == 554947552865):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:40QTqOBBxCEIQlLNdSjFQB')
               sleep(2)

           elif (id == 489130600001):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:50yFYgKdwJANZ5O9MIbMkg')
               sleep(2)

           elif (id ==420444677719 ):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:artist:2QsynagSdAqZj3U9HgDzjD')
               sleep(2)
               
           elif (id == 831905965731):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1Mhn9VosyjtWn4dMPFlna6')
               sleep(2)
               
           elif (id == 488456889889):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7gsWAHLeT0w7es6FofOXk1')
               sleep(2)
               
           elif (id == 209169294039):

               # playing an album
               sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:22GvFtvyMX6DUWmX0i6x1X'])
               sleep(2)

   # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
   except Exception as e:
       print(e)
       pass

   finally:
       print("Cleaning  up...")
       GPIO.cleanup()

