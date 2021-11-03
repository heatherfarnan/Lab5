#!/usr/bin/python37all

import RPi.GPIO as GPIO
import time

from stepper import Stepper

step = Stepper(0x48)

ledPin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

import json

print("i've gotten this far in this code 1")

while True:
  with open("Lab5.txt", 'r') as f:
    values = json.load(f)
    position = float(values['slider1']) #f.read()) # read duty cycle value from file
    zero = str(values['zeroing'])
  f.close()


  print("i've gotten this far in this code 2 {}".format(zero))

  if "zero" in zero:
    step.zero() 
    print("zero attemptted {}".format(position))

    with open("Lab5.txt", 'w') as h:
      h.write({'slider1':0, 'zeroing':0})
    h.close()

    print(zero)

  time.sleep(0.1)
#change