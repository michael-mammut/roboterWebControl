import RPi.GPIO as GPIO
from .GpioPinConfig import GpioPinConfig as pin

class GpioConfiHelper:
    # Set all Pins to low
    def all_off(self):
        GPIO.output(pin.ENABLE_ENGINE_A, False)
        GPIO.output(pin.ENABLE_ENGINE_B, False)
        GPIO.output(pin.INPUT1, False)
        GPIO.output(pin.INPUT2, False)
        GPIO.output(pin.INPUT3, False)
        GPIO.output(pin.INPUT4, False)
        return "ALL GPIOS OFF"

    # Define all Pins to output
    def all_out(self):
        GPIO.setup(pin.ENABLE_ENGINE_A, GPIO.OUT)
        GPIO.setup(pin.ENABLE_ENGINE_B, GPIO.OUT)
        GPIO.setup(pin.INPUT1, GPIO.OUT)
        GPIO.setup(pin.INPUT2, GPIO.OUT)
        GPIO.setup(pin.INPUT3, GPIO.OUT)
        GPIO.setup(pin.INPUT4, GPIO.OUT)
        return "ALL GPIOS OUTPUT"