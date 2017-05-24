from movementDirection.movements import Direction
import RPi.GPIO as GPIO
from ..config.GpioPinConfig import GpioPinConfig as pin

class Forward(Direction):
    def direction(self):
       GPIO.output(pin.ENABLE_ENGINE_A, True)
       GPIO.output(pin.ENABLE_ENGINE_B, True)
       GPIO.output(pin.INPUT1, True)
       GPIO.output(pin.INPUT2, True)
       GPIO.output(pin.INPUT3, True)
       GPIO.output(pin.INPUT4, True)
       return "FORWARD"

