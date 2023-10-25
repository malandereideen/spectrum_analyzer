import machine
from machine import I2S
from neopixel import NeoPixel

#Neopixel Pin
pin = machine.Pin(2,machine.Pin.OUT)
#Neopixel definieren mit Pin und Anzahl
np = NeoPixel(pin,60)

#Microphone I2S Config
bck_pin = machine.Pin(26)
ws_pin = machine.Pin(25)
sdin_pin = machine.Pin(22)

audio = I2S(0, 
            sck=bck_pin, 
            ws=ws_pin, 
            sd=sdin_pin, 
            mode=I2S.RX,
            bits=16,
            format=I2S.MONO,
            rate=16000, 
            ibuf=9600)

while True:
    audio_samples = bytearray(1024)
    numread = audio.readinto(audio_samples)
    if numread > 0:
        # Verarbeitung der audio_samples hier...
        print(audio_samples)