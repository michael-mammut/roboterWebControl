from movementDirection.movements.Direction import DirectionAbstract
import RPi.GPIO as GPIO
from ..config.GpioPinConfig import GpioPinConfig as pin

class Forward(DirectionAbstract):

    def direction(self):
       GPIO.output(pin.ENABLE_ENGINE_A, str(1))
       GPIO.output(pin.ENABLE_ENGINE_B, str(1))
       GPIO.output(pin.INPUT1, str(1))
       GPIO.output(pin.INPUT2, str(0))
       GPIO.output(pin.INPUT3, str(1))
       GPIO.output(pin.INPUT4, str(0))
       return "FORWARD"

