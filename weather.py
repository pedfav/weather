# -*- coding: utf-8 -*-

from Data import Data
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import time
import datetime
import pymongo
from flask import Flask,jsonify,json

app = Flask(__name__)
with app.app_context():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    myclient = pymongo.MongoClient("mongodb://192.168.0.18:27017")
    mydb = myclient["test"]
    mycol = mydb["weather"]

    # formata os dados de saída
    while(1):
        if GPIO.input(4):
            #Efetua leitura (Tipo dht, gpio usado)
            umidade, temperatura = DHT.read_retry(22, 25)

            if umidade is not None and temperatura is not None:
                GPIO.output(24, GPIO.HIGH)
                data = Data(temperatura, umidade)
                data.to_string()
                mycol.insert_one(data.to_json())
                time.sleep(1)

                GPIO.output(24, GPIO.LOW)
            else:
                print('Não foi possível obter nenhuma leitura')
        time.sleep(2)
