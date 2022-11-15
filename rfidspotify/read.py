#!/usr/bin/env python
#client: 38d6c9a24eec445288edb097eafc59dc
#secret: ba41a77481be4f4b865cc77ad0cdf65b
#98bb0735e28656bac098d927d410c3138a4b5bca
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        print("Waiting for you to scan an RFID sticker/card")
        id = reader.read()[0]
        print("The ID for this card is:", id)
        
finally:
        GPIO.cleanup()