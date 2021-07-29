#Include libraries
import RPi.GPIO as GPIO 
import time
from RPLCD.gpio import CharLCD

# Configure the LCD
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

# Create a variable ‘number’ 
number=0

# Main loop
while(True):
  number=number + 1
  lcd.write_string("Count:"  + str(number))
  time.sleep(1) 
  lcd.close()
