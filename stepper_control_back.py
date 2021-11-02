#!/usr/bin/python37all

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time

ledPin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

import json

# with open("test.txt", 'w') as o:
#   o.write("i've gotten this far in this code")

while True:
  with open("lab5.txt", 'r') as f:
    values = json.load(f)
    position = float(values['slider1']) #f.read()) # read duty cycle value from file
    speed = float(values['option'])

  with open("test.txt", 'w') as o:
    o.write("i've gotten this far in this code heyo {}".format(position))

  if "a" in activeled:
    pwm1.ChangeDutyCycle(dutyCycle)



  time.sleep(0.1)
#change