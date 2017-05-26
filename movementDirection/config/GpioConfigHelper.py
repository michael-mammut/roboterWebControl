import RPi.GPIO as GPIO

from .GpioPinConfig import GpioPinConfig as pin


class GpioConfiHelper:
    # Set all Pins to low
    def all_off(self):
        GPIO.output(pin.ENABLE_ENGINE_A, str(0))
        GPIO.output(pin.ENABLE_ENGINE_B, str(0))
        GPIO.output(pin.INPUT1, str(0))
        GPIO.output(pin.INPUT2, str(0))
        GPIO.output(pin.INPUT3, str(0))
        GPIO.output(pin.INPUT4, str(0))
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