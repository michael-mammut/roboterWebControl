from movementDirection.movements.Direction import DirectionAbstract
import RPi.GPIO as GPIO
from ..config.GpioPinConfig import GpioPinConfig as pin

class Forward(DirectionAbstract):

    def direction(self):
       GPIO.output(pin.ENABLE_ENGINE_A, 1)
       GPIO.output(pin.ENABLE_ENGINE_B, 1)
       GPIO.output(pin.INPUT1, 1)
       GPIO.output(pin.INPUT2, 0)
       GPIO.output(pin.INPUT3, 1)
       GPIO.output(pin.INPUT4, 0)
       return "FORWARD"

