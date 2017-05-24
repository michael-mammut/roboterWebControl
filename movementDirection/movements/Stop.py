from movementDirection.movements import Direction
import RPi.GPIO as GPIO
from ..config.GpioPinConfig import GpioPinConfig as pin

class Stop(Direction):
    def direction(self):
       GPIO.output(pin.ENABLE_ENGINE_A, False)
       GPIO.output(pin.ENABLE_ENGINE_B, False)
       GPIO.output(pin.INPUT1, False)
       GPIO.output(pin.INPUT2, False)
       GPIO.output(pin.INPUT3, False)
       GPIO.output(pin.INPUT4, False)
       return "STOP"
