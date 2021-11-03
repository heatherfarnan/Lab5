from PCF8591 import PCF8591

# class photo:
#hey

#   def __init__ (self, address):
#     self.PCF = PCF8591(address)

#   def readPhoto(self):
#     return self.PCF.read(0)

class Stepper:

  def __init__ (self, address):
    self.PCF = PCF8591(address)

  # def getAngle(self):
  
  # Make a full rotation of the output shaft:
  # def loop(dir): # dir = rotation direction (cw or ccw)
  #   for i in range(512): # full revolution (8 cycles/rotation * 64 gear ratio)
  #     for halfstep in range(8): # 8 half-steps per cycle
  #       for pin in range(4):    # 4 pins that need to be energized
  #         GPIO.output(pins[pin], dir[halfstep][pin])
  #       delay_us(1000)

    # return self.#idk

  def zero(self):
    ledPin = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)

    ledState = 1
    GPIO.output(ledPin, ledState)

    photo = self.PCF.read(0)
    while photo >= 205:
      photo = self.PCF.read(0)
      print(photo)
      moveSteps(1,1)
    ledState = 0
    return self.PCF.read(0) 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0 #current position in stator sequence
# photo = 200 #value of photoresistor. tip point point is 205

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir = +/- 1 (ccw / cw)
  global state
  state += dir
  if state > 7: state = 0
  elif state < 0: state = 7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000)


def moveSteps(steps, dir):
  #move the actuation sequence a given number of half steps
  for step in range(steps):
    halfstep(dir)


#further modify this code
#convert it into a class
#use instance methods for that object to get the motor to move the way you want
#2 new methods: given angle (what's and angle? it's relative to zero. should be able to convert: certain angular resolution associated with a single half step --> how many half steps are needed to go from current angle to desired angle?
#speaking of which we also need to keep track of current angle
#input angel is absolute relative to absolute zero. positive angle between 0 and 360