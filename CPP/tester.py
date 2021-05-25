#!/usr/bin/python3

import time
import encoder

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

encoder.initialise()
encoder1 = encoder.Encoder(23, 24)
while True:
    print(encoder1.getSteps())
    time.sleep(1)
