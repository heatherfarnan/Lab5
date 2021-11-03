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
  position = 0
  with open("Lab5.txt", 'r') as f:
    values = json.load(f)
    position = float(values['slider1']) #f.read()) # read duty cycle value from file
    zero = str(values['zeroing'])
  f.close()

  if "zero" in zero:
    step.zero() 

    with open("Lab5.txt", 'w') as h:
      h.write('''{"slider1":"0", "zeroing":"0"}''')
    h.close()


  if position != 0:
    n = int(4000*position/360) 
    print('n = %f' %n)
    step.goAngle(n) 

    with open("Lab5.txt", 'w') as g:
      g.write('''{"slider1":"0", "zeroing":"0"}''')
    g.close()


  time.sleep(.5)
#change