from movementDirection.movements.Direction import DirectionAbstract
import RPi.GPIO as GPIO
from ..config.GpioPinConfig import GpioPinConfig as pin

class Forward(DirectionAbstract):

    def direction(self):
       GPIO.output(pin.ENABLE_ENGINE_A.value, str(1))
       GPIO.output(pin.ENABLE_ENGINE_B.value, str(1))
       GPIO.output(pin.INPUT1.value, str(1))
       GPIO.output(pin.INPUT2.value, str(0))
       GPIO.output(pin.INPUT3.value, str(1))
       GPIO.output(pin.INPUT4.value, str(0))
       return "FORWARD"

