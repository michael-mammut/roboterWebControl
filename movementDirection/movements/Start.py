from movementDirection.config.GpioConfigHelper import GpioConfiHelper
from movementDirection.movements.Direction import DirectionAbstract

class Start(DirectionAbstract):

   def direction(self):
       helper = GpioConfiHelper()
       helper.all_off()
       helper.all_out()

       return "Engine configured and able to start"
