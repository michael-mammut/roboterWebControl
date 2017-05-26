from movementDirection.movements.Direction import DirectionAbstract
from time import sleep
import RPi.GPIO as GPIO
from ..config.GpioPinConfig import GpioPinConfig as pin
from ..config.GpioConfigHelper import GpioConfiHelper

class Right(DirectionAbstract):

    def direction(self):
       GPIO.output(pin.ENABLE_ENGINE_A.value, 1)
       GPIO.output(pin.ENABLE_ENGINE_B.value, 1)
       GPIO.output(pin.INPUT1.value, 0)
       GPIO.output(pin.INPUT2.value, 1)
       GPIO.output(pin.INPUT3.value, 1)
       GPIO.output(pin.INPUT4.value, 0)

       sleep(1)

       helper = GpioConfiHelper()
       helper.all_off()

       return "RIGHT"

