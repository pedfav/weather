# -*- coding: utf-8 -*-
import Adafruit_DHT
from datetime import datetime


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

  if humidity is not None and temperature is not None:
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(temperature)
  else:
    print("Fail to get data from dht22")

  time.sleep(10)