# -*- coding: utf-8 -*-
import Adafruit_DHT
import time
from datetime import datetime
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import socket
import requests

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

  if humidity is not None and temperature is not None:
    lcd.clear()
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    lcd.write_string(now)
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"T={round(temperature, 2)} - H={round(humidity, 2)}")
    print(f"Time={now} - Temperature={round(temperature, 2)} - Humidity={round(humidity, 2)}")

    time.sleep(4)

    lcd.clear()
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    lcd.write_string(now)
    lcd.cursor_pos=(1,0)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    lcd.write_string(f"IP={s.getsockname()[0]}")
    print(f"IP={s.getsockname()[0]}")

    time.sleep(4)

    lcd.clear()
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    lcd.write_string(now)
    lcd.cursor_pos=(1,0)
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc = data["bpi"]["USD"]["rate"]
    lcd.write_string(f"BTC={btc}")
    print(f"BTC={btc}")

  else:
    print("Fail to get data from dht22")

  time.sleep(4)