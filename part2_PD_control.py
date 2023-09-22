#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sound import Sound
from time import sleep

ultrasonic = UltrasonicSensor()
sound = Sound()

DESIRED_DISTANCE_CM = 10
Kp = 10 
Kd = 10
offset = 10 # Offset for zero error conditions

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)


sound.speak('Commencing P D control')
previous_error = 0

while True:
  measured_distance = ultrasonic.distance_centimeters

  error = measured_distance - DESIRED_DISTANCE_CM
  delta_error = error - previous_error

  output_speed = (Kp * error) + (Kd * delta_error) + offset

  tank_pair.on(left_speed = output_speed, right_speed = output_speed)



  



