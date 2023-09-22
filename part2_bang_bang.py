#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sound import Sound
from time import sleep

ultrasonic = UltrasonicSensor()
sound = Sound()

DESIRED_DISTANCE_CM = 10
Kbb = 50 #fixed magnitude gain representing speed at which motor moves
offset = 25 # Offset for zero error conditions

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

sound.speak('Commencing bang bang control')
while True:
  measured_distance = ultrasonic.distance_centimeters
  error_sign = 1 if measured_distance > DESIRED_DISTANCE_CM else -1

  output_speed = (Kbb * error_sign) + offset

  tank_pair.on(left_speed = output_speed, right_speed = output_speed)



  



