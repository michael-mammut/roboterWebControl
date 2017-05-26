import RPi.GPIO as GPIO

from .GpioPinConfig import GpioPinConfig as pin


class GpioConfiHelper:
    # Set all Pins to low
    def all_off(self):
        GPIO.output(pin.ENABLE_ENGINE_A.value, str(0))
        GPIO.output(pin.ENABLE_ENGINE_B.value, str(0))
        GPIO.output(pin.INPUT1.value, str(0))
        GPIO.output(pin.INPUT2.value, str(0))
        GPIO.output(pin.INPUT3.value, str(0))
        GPIO.output(pin.INPUT4.value, str(0))
        return "ALL GPIOS OFF"

    # Define all Pins to output
    def all_out(self):
        GPIO.setup(pin.ENABLE_ENGINE_A.value, GPIO.OUT)
        GPIO.setup(pin.ENABLE_ENGINE_B.value, GPIO.OUT)
        GPIO.setup(pin.INPUT1.value, GPIO.OUT)
        GPIO.setup(pin.INPUT2.value, GPIO.OUT)
        GPIO.setup(pin.INPUT3.value, GPIO.OUT)
        GPIO.setup(pin.INPUT4.value, GPIO.OUT)
        return "ALL GPIOS OUTPUT"