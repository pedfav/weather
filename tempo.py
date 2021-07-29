# -*- coding: utf-8 -*-
import Adafruit_DHT
import time
from datetime import datetime
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

  if humidity is not None and temperature is not None:
    lcd.clear()
    now = datetime.now().strftime("%H:%M:%S")

    lcd.write_string(f"Time={now}")
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"T={round(temperature, 2)} - H={round(humidity, 2)}")
    print(f"Time={now} - Temperature={round(temperature, 2)} - Humidity={round(humidity, 2)}")

  else:
    print("Fail to get data from dht22")

  time.sleep(2)