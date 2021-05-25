#!/usr/bin/env python

# import pigpio
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Encoder:

    """Class to decode mechanical rotary encoder pulses."""

    def __init__(self, gpioA, gpioB):

        """
        Instantiate the class with the pi and gpios connected to
        rotary encoder contacts A and B.  The common contact
        should be connected to ground.  The callback is
        called when the rotary encoder is turned.  It takes
        one parameter which is +1 for clockwise and -1 for
        counterclockwise.
        """
    
        self.gpioA = gpioA
        self.gpioB = gpioB

        self.steps = 0

        self.levA = 0
        self.levB = 0

        self.lastGpio = None

        GPIO.setup(gpioA, GPIO.IN)
        GPIO.setup(gpioB, GPIO.IN)

        GPIO.add_event_detect(gpioA, GPIO.BOTH, callback = self._pulse)
        GPIO.add_event_detect(gpioB, GPIO.BOTH, callback = self._pulse)

    def _pulse(self, gpio):

        """
        Decode the rotary encoder pulse.

                    +---------+         +---------+      0
                    |         |         |         |
                    |         |         |         |
                    |         |         |         |
          +---------+         +---------+         +----- 1

                +---------+         +---------+           0
                |         |         |         |
            B   |         |         |         |
                |         |         |         |
            ----+         +---------+         +--------+ 1
        """

        level = GPIO.input(gpio)

        if gpio == self.gpioA:
            self.levA = level
        else:
            self.levB = level

        if gpio != self.lastGpio: # debounce
            self.lastGpio = gpio

            if gpio == self.gpioA and level == 1:
                if self.levB == 1:
                    self.steps += 1
            elif gpio == self.gpioB and level == 1:
                if self.levA == 1:
                    self.steps -= 1
                    print("Not working")

if __name__ == "__main__":

    import time

    encoder1 = Encoder(23, 24)

    time.sleep(3)

