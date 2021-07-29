# -*- coding: utf-8 -*-
import Adafruit_DHT
import time
from datetime import datetime

import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

lcd = CharLCD(pin_rs=19, pin_e=16, pin_rw=None, pins_data=[23, 17, 21, 22], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

  if humidity is not None and temperature is not None:
    lcd.clear()
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    lcd.write_string(f"Date={now} - Temperature={temperature} - Humidity={humidity}")
    print(f"Date={now} - Temperature={temperature} - Humidity={humidity}")

    lcd.close() 
    GPIO.cleanup()
  else:
    print("Fail to get data from dht22")

  time.sleep(2)