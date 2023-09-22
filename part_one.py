#!/usr/bin/env python3

from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep

sound = Sound()
color = ColorSensor()



tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

def calibrate():
  """ Calibration function """
  sound.speak('Commencing calibration')
  sleep(0.5)
  sound.speak('Put sensor on white')
  sleep(1.0)
  white_val = color.reflected_light_intensity # Read white
  sleep(0.5)
  sound.speak('Put sensor on black')
  sleep(1.0)
  black_val = color.reflected_light_intensity # Read black

  global threshold_val # global variable for threshold
  threshold_val = (white_val + black_val) / 2 # Compute threshold from average

  sound.speak('Calibration Completed')


def follow_line():
  """ Line following function for following the left side of the line """
  while True:
    # Reading sensor value on each iteration
    input_val = color.reflected_light_intensity

    if input_val < threshold_val: # on black, turn left
      tank_pair.on(left_speed = 0, right_speed= 30)
    elif input_val > threshold_val:  # on white, turn right
      tank_pair.on(left_speed=30, right_speed=0)
    
    sleep(0.01) # Sleep to not max out the CPU





""" EXECUTION """
calibrate()
follow_line()


